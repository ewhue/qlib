#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic Qlib Example
This example shows how to use Qlib without compiled extensions
"""

import os
import sys

# Add the qlib path to avoid import issues
sys.path.insert(0, 'D:/gitub/qlib')

def main():
    print("=" * 60)
    print("Basic Qlib Usage Example")
    print("=" * 60)
    
    # 1. Check Qlib installation
    print("\n1. Checking Qlib installation...")
    try:
        import qlib
        print(f"   Success: Qlib version {qlib.__version__} found!")
    except ImportError as e:
        print(f"   Error: Cannot import qlib: {e}")
        return
    
    # 2. Show basic configuration
    print("\n2. Basic Qlib configuration:")
    try:
        from qlib.constant import REG_CN, REG_US
        print(f"   Available regions: CN={REG_CN}, US={REG_US}")
        
        # Show data path
        data_path = os.path.expanduser("~/.qlib/qlib_data/cn_data")
        print(f"   Default data path: {data_path}")
        print(f"   Data path exists: {os.path.exists(data_path)}")
        
    except Exception as e:
        print(f"   Error: {e}")
    
    # 3. Show available models
    print("\n3. Available model examples:")
    examples_path = "D:/gitub/qlib/examples/benchmarks"
    if os.path.exists(examples_path):
        models = [d for d in os.listdir(examples_path) 
                 if os.path.isdir(os.path.join(examples_path, d)) and d != '__pycache__']
        print(f"   Found {len(models)} model examples:")
        for i, model in enumerate(models[:10], 1):  # Show first 10
            print(f"   {i:2d}. {model}")
        if len(models) > 10:
            print(f"   ... and {len(models) - 10} more")
    else:
        print("   Examples directory not found")
    
    # 4. Show workflow configurations
    print("\n4. Available workflow configurations:")
    config_files = []
    for root, dirs, files in os.walk("D:/gitub/qlib/examples"):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                config_files.append(os.path.join(root, file))
    
    print(f"   Found {len(config_files)} configuration files:")
    for i, config in enumerate(config_files[:5], 1):  # Show first 5
        rel_path = config.replace("D:/gitub/qlib/", "")
        print(f"   {i}. {rel_path}")
    if len(config_files) > 5:
        print(f"   ... and {len(config_files) - 5} more")
    
    # 5. Basic usage instructions
    print("\n5. How to use Qlib:")
    print("   Step 1: Download data")
    print("   Command: python -m qlib.run.get_data qlib_data --target_dir ~/.qlib/qlib_data/cn_data --region cn")
    print("   ")
    print("   Step 2: Run a simple model")
    print("   Command: qrun examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml")
    print("   ")
    print("   Step 3: View results")
    print("   Results will be saved in mlruns/ directory")
    
    # 6. Data download helper
    print("\n6. Data download options:")
    print("   Option 1: Official data (currently unavailable)")
    print("   Command: python -m qlib.run.get_data qlib_data --target_dir ~/.qlib/qlib_data/cn_data --region cn")
    print("   ")
    print("   Option 2: Community data")
    print("   Download: https://github.com/chenditc/investment_data/releases/latest/download/qlib_bin.tar.gz")
    print("   Extract to: ~/.qlib/qlib_data/cn_data")
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("")
    print("Next steps:")
    print("1. Download data using one of the methods above")
    print("2. Try running: qrun examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml")
    print("3. Explore other models in examples/benchmarks/")
    print("4. Read documentation at: https://qlib.readthedocs.io/")
    print("=" * 60)

if __name__ == "__main__":
    main()