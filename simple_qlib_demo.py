#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple Qlib Demo Script
This script demonstrates basic Qlib functionality
"""

import qlib
from qlib.constant import REG_CN

def main():
    print("=" * 50)
    print("Welcome to Qlib Quantitative Investment Platform Demo")
    print("=" * 50)
    
    # 1. Initialize Qlib
    print("\n1. Initializing Qlib...")
    provider_uri = "~/.qlib/qlib_data/cn_data"
    
    try:
        qlib.init(provider_uri=provider_uri, region=REG_CN)
        print("   Success: Qlib initialized!")
        print(f"   Qlib version: {qlib.__version__}")
        
    except Exception as e:
        print(f"   Error: Initialization failed: {e}")
        print("   Note: You may need to download data first")
        return
    
    # 2. Basic data operations
    print("\n2. Demonstrating basic data operations...")
    try:
        from qlib.data import D
        
        # Get trading calendar
        print("   Getting trading calendar (last 5 days):")
        calendar = D.calendar(start_time='2020-01-01', end_time='2020-01-10', freq='day')
        print(f"   {calendar[:5].tolist()}")
        
        # Get stock list
        print("   Getting CSI300 stock list (first 5):")
        instruments = D.instruments('csi300')
        stock_list = D.list_instruments(instruments=instruments, start_time='2020-01-01', end_time='2020-01-10', as_list=True)
        print(f"   {stock_list[:5]}")
        
        # Get stock data
        print("   Getting stock feature data:")
        instruments = ['SH600000']  # SPDB
        fields = ['$close', '$volume', 'Ref($close, 1)', 'Mean($close, 3)', '$high-$low']
        data = D.features(instruments, fields, start_time='2020-01-01', end_time='2020-01-10', freq='day')
        print("   Data sample:")
        print(data.head())
        
        print("   Success: Data operations completed!")
        
    except Exception as e:
        print(f"   Error: Data operations failed: {e}")
        print("   This might be because data is not downloaded yet")
    
    # 3. Show configuration
    print("\n3. Qlib Configuration:")
    try:
        print(f"   Qlib version: {qlib.__version__}")
        print(f"   Data path: {provider_uri}")
        print(f"   Region: {REG_CN}")
        print("   Success: Configuration displayed!")
    except Exception as e:
        print(f"   Error: Failed to get configuration: {e}")
    
    print("\n" + "=" * 50)
    print("Qlib Demo Completed!")
    print("Next steps:")
    print("1. Run examples/workflow_by_code.py for complete workflow")
    print("2. Use qrun command to run predefined strategies")
    print("3. Check examples/benchmarks/ for various model examples")
    print("=" * 50)

if __name__ == "__main__":
    main()