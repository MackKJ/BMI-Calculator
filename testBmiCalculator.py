import unittest
from bmiCalculator import heightToInches, inchesToMeters, poundsToKilos, calculateBMI, calculateCategory

class TestBMICalculator(unittest.TestCase):

    #Height to inches tests
    def test_heightToInches(self):
        inches = heightToInches(5, 11)
        self.assertEqual(inches, 71)
        
    def test_heightToInches_zeros(self):
        inches = heightToInches(0, 0)
        self.assertEqual(inches, 0)

    def test_heightToInches_negative_feet(self):
        with self.assertRaises(ValueError):
            heightToInches(-5, 4)
            
    def test_heightToInches_negative_inches(self):
        with self.assertRaises(ValueError):
            heightToInches(5, -7)
        
    def test_heightToInches_non_numeric_feet(self):
        with self.assertRaises(TypeError):
            heightToInches('a', 6)
            
    def test_heightToInches_non_numeric_inches(self):
        with self.assertRaises(TypeError):
            heightToInches(5, 'a')
       
    #Inches to meters tests     
    def test_inchesToMeters(self):
        meters = inchesToMeters(71)
        self.assertEqual(meters, 1.78)

    def test_inchesToMeters_zero(self):
        meters = inchesToMeters(0)
        self.assertEqual(meters, 0)
        
    def test_inchesToMeters_negative(self):
        with self.assertRaises(ValueError):
            inchesToMeters(-5)
            
    def test_inchesToMeters_non_numeric(self):
        with self.assertRaises(TypeError):
            inchesToMeters('a')
        
    #Pounds to kilos tests    
    def test_poundsToKilos(self):
        meters = poundsToKilos(165)
        self.assertEqual(meters, 74.25)

    def test_poundsToKilos_zero(self):
        meters = poundsToKilos(0)
        self.assertEqual(meters, 0)
        
    def test_poundsToKilos_negative(self):
        with self.assertRaises(ValueError):
            poundsToKilos(-87)
            
    def test_poundsToKilos_non_numeric(self):
        with self.assertRaises(TypeError):
            poundsToKilos('a')
        
    #Calculate BMI tests    
    def test_calculatBMI(self):
        bmi = calculateBMI(1.78, 74.25)
        self.assertEqual(bmi, 23.4)

    def test_calculatBMI_zeros(self):
        with self.assertRaises(ZeroDivisionError):
            calculateBMI(0, 0)
    
    def test_calculatBMI_negative_height(self):
        with self.assertRaises(ValueError):
            calculateBMI(-5, 74.25)
            
    def test_calculatBMI_negative_weight(self):
        with self.assertRaises(ValueError):
            calculateBMI(1.78, -5)
            
    def test_calculatBMI_non_numeric_height(self):
        with self.assertRaises(TypeError):
            calculateBMI('a', 74.25)
            
    def test_calculatBMI_non_numeric_weight(self):
        with self.assertRaises(TypeError):
            calculateBMI(1.78, 'a')
            
    #Calculate category tests
    def test_calculateCategory_underweight(self):
        category = calculateCategory(18.4)
        self.assertEqual(category, "Underweight")
 
    def test_calculateCategory_normal_low(self):
        category = calculateCategory(18.5)
        self.assertEqual(category, "Normal weight")
    
    def test_calculateCategory_normal_high(self):
        category = calculateCategory(24.9)
        self.assertEqual(category, "Normal weight")
        
    def test_calculateCategory_overweight_low(self):
        category = calculateCategory(25)
        self.assertEqual(category, "Overweight")
        
    def test_calculateCategory_overweight_high(self):
        category = calculateCategory(29.9)
        self.assertEqual(category, "Overweight")
    
    def test_calculateCategory_obese(self):
        category = calculateCategory(30)
        self.assertEqual(category, "Obese")
        
        
if __name__ == '__main__':
    unittest.main()