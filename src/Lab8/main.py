import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from classes.AdvancedVisualizer import AdvancedVisualizer
from classes.BasicVisualizer import BasicVisualizer
from classes.DataAnalyzer import DataAnalyzer
from classes.DataPreparer import DataPreparer
from classes.MultiPlotVisualizer import MultiPlotVisualizer
from loaders.dataLoader import DataLoader

def main():
    filepath = "C:/Users/Користувач/Desktop/5 семестр/SMP/SMP/source/CarsCSV.csv"
    loader = DataLoader(filepath)
    data = loader.get_data()
    
    analyzer = DataAnalyzer(data)
    print(analyzer.get_extreme_values())
    
    preparer = DataPreparer(data)
    prepared_data = preparer.prepare_data_for_visualization()
    
    basic_vis = BasicVisualizer(prepared_data)
    basic_vis.plot_line_chart('Fuel_Type__c', 'Sale_Price__c')
    
    adv_vis = AdvancedVisualizer(prepared_data)
    adv_vis.plot_bar_chart('Engine_Power__c', 'Sale_Price__c')
    
    multi_vis = MultiPlotVisualizer(prepared_data)
    multi_vis.plot_multiple()

if __name__ == "__main__":
    main()