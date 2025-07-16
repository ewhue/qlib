# -*- coding: utf-8 -*-
"""
Qlib 使用教程演示
这个脚本提供了一个完整的Qlib使用示例，从初始化到模型训练和预测。
"""

import qlib
import pandas as pd
from qlib.constant import REG_CN
from qlib.utils import init_instance_by_config
from qlib.data import D
from qlib.workflow import R
from qlib.workflow.record_temp import SignalRecord, PortAnaRecord
import os
import mlflow

def main():
    print("=" * 60)
    print("Qlib 使用教程演示")
    print("=" * 60)
    
    # 结束之前的MLflow运行
    try:
        mlflow.end_run()
    except:
        pass
    
    # 步骤1: 初始化 Qlib
    print("\n1. 初始化 Qlib")
    provider_uri = os.path.expanduser("~/.qlib/qlib_data/cn_data")
    qlib.init(provider_uri=provider_uri, region=REG_CN)
    print("   ✓ 初始化完成！")
    
    # 步骤2: 数据操作
    print("\n2. 基本数据操作")
    # 获取交易日历
    calendar = D.calendar(start_time='2023-01-01', end_time='2023-01-10')
    print("   交易日历:", calendar)
    
    # 获取股票列表
    instruments = D.instruments(market='csi300')
    stock_list = D.list_instruments(instruments, as_list=True)[:5]
    print("   CSI300 前5只股票:", stock_list)
    
    # 获取特征数据
    data = D.features(['SH600000'], ['$close', '$volume'], start_time='2023-01-01', end_time='2023-01-10')
    print("   数据样例:\n", data.head())
    
    # 步骤3: 模型训练和预测
    print("\n3. 模型训练和预测")
    # 示例任务配置
    task = {
        "model": {"class": "LGBModel", "module_path": "qlib.contrib.model.gbdt"},
        "dataset": {
            "class": "DatasetH",
            "module_path": "qlib.data.dataset",
            "kwargs": {
                "handler": {"class": "Alpha158", "module_path": "qlib.contrib.data.handler", "kwargs": {"instruments": "csi300"}},
                "segments": {"train": ("2008-01-01", "2014-12-31"), "valid": ("2015-01-01", "2016-12-31"), "test": ("2017-01-01", "2020-08-01")}
            }
        }
    }
    model = init_instance_by_config(task["model"])
    dataset = init_instance_by_config(task["dataset"])
    model.fit(dataset)
    print("   ✓ 模型训练完成！")
    
    # 预测
    pred = model.predict(dataset)
    print("   预测结果样例:\n", pred.head())
    
    # 步骤4: 简单的结果分析
    print("\n4. 简单的结果分析")
    # 计算预测统计信息
    print(f"   预测值数量: {len(pred)}")
    print(f"   预测值范围: [{pred.min():.4f}, {pred.max():.4f}]")
    print(f"   预测值均值: {pred.mean():.4f}")
    print(f"   预测值标准差: {pred.std():.4f}")
    print("   ✓ 结果分析完成！")
    
    print("\n演示结束！您可以修改参数进行实验。")

if __name__ == "__main__":
    main()