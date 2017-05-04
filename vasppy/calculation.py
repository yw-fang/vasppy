import yaml
import re
from collections import Counter

class Calculation:
    """
    class describing a single VASP calculation
    """
    
    def __init__( self, title, energy, stoichiometry ):
        """
        Initialise a Calculation object

        Args:
            title (Str): The title string for this calculation.
            energy (Float): Final energy in eV.
            stoichiometry (Dict{Str:Int}): A dict desribing the calculation stoichiometry,
                e.g. { 'Ti': 1, 'O': 2 }

        Returns:
            None
        """
        self.title = title
        self.energy = energy
        self.stoichiometry = Counter( stoichiometry )
        
    def __mul__( self, scaling ):
        """
        "Multiply" this Calculation by a scaling factor.
        Returns a new Calculation with the same title, but scaled energy and stoichiometry.

        Args:
            scaling (float): The scaling factor.

        Returns:
            (vasppy.Calculation): The scaled Calculation.
        """
        new_calculation = Calculation( title=self.title, energy=self.energy*scaling, stoichiometry=self.scale_stoichiometry( scaling ) )
        return new_calculation
        
    def __truediv__( self, scaling ):
        """
        Implements division by a scaling factor.
        Returns a new Calculation with the same title, but scaled energy and stoichiometry.

        Args:
            scaling (float): The scaling factor.

        Returns:
            (vasppy.Calculation): The scaled Calculation.
        """

        return self * ( 1 / scaling )
        
    def scale_stoichiometry( self, scaling ):
        return { k:v*scaling for k,v in self.stoichiometry.items() }
    
def delta_E( reactants, products, check_balance=True ):
    if check_balance:
        if delta_stoichiometry( reactants, products ) != {}:
            raise ValueError( "reaction is not balanced: {}".format( delta_stoichiometry( reactants, products) ) )
    return sum( [ r.energy for r in products ] ) - sum( [ r.energy for r in reactants ] )

def delta_stoichiometry( reactants, products ):
    totals = Counter()
    for r in reactants:
        totals.update( ( r * -1.0 ).stoichiometry )
    for p in products:
        totals.update( p.stoichiometry )
    to_return = {}
    for c in totals:
        if totals[c] != 0:
            to_return[c] = totals[c]
    return to_return

def energy_string_to_float( string ):
    energy_re = re.compile( "(-?\d+\.\d+)" )
    return float( energy_re.match( string )[0] )
    
def import_calculations_from_file( filename ):
    calcs = {}
    with open( filename, 'r' ) as stream:
        docs = yaml.load_all( stream )
        for d in docs:
            stoichiometry = Counter()
            for s in d['stoichiometry']:
                stoichiometry.update( s )
            calcs[ d['title'] ] = Calculation( title=d['title'], 
                                               stoichiometry=stoichiometry, 
                                               energy=energy_string_to_float( d['energy'] ) )
    return calcs