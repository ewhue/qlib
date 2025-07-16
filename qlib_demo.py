#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Qlib 演示脚本
这个脚本展示了如何使用 Qlib 进行基本的量化投资研究
"""

import qlib
import pandas as pd
from qlib.constant import REG_CN
from qlib.utils import init_instance_by_config
from qlib.workflow import R
from qlib.workflow.record_temp import SignalRecord, PortAnaRecord, SigAnaRecord
from qlib.tests.data import GetData
from qlib.tests.config import CSI300_BENCH, CSI300_GBDT_TASK

# 运行我们创建的演示脚本

    print("=" * 50)
    print("欢迎使用 Qlib 量化投资平台演示")
    print("=" * 50)
    
    # 1. 初始化 Qlib
    print("\n1. 正在初始化 Qlib...")
    provider_uri = "~/.qlib/qlib_data/cn_data"
    
    try:
        # 尝试获取数据（如果不存在的话）
        print("   检查并下载数据...")
        GetData().qlib_data(target_dir=provider_uri, region=REG_CN, exists_skip=True)
        
        # 初始化 Qlib
        qlib.init(provider_uri=provider_uri, region=REG_CN)
        print("   ✓ Qlib 初始化成功！")
        
    except Exception as e:
        print(f"   ✗ 初始化失败: {e}")
        print("   提示：请确保网络连接正常，或手动下载数据")
        return
    
    # 2. 展示基本数据操作
    print("\n2. 展示基本数据操作...")
    try:
        from qlib.data import D
        
        # 获取交易日历
        print("   获取交易日历（最近5天）:")
        calendar = D.calendar(start_time='2020-01-01', end_time='2020-01-10', freq='day')
        print(f"   {calendar[:5].tolist()}")
        
        # 获取股票列表
        print("   获取CSI300股票列表（前5只）:")
        instruments = D.instruments('csi300')
        stock_list = D.list_instruments(instruments=instruments, start_time='2020-01-01', end_time='2020-01-10', as_list=True)
        print(f"   {stock_list[:5]}")
        
        # 获取股票数据
        print("   获取股票特征数据:")
        instruments = ['SH600000']  # 浦发银行
        fields = ['$close', '$volume', 'Ref($close, 1)', 'Mean($close, 3)', '$high-$low']
        data = D.features(instruments, fields, start_time='2020-01-01', end_time='2020-01-10', freq='day')
        print("   数据样例:")
        print(data.head())
        
        print("   ✓ 数据操作演示完成！")
        
    except Exception as e:
        print(f"   ✗ 数据操作失败: {e}")
        print("   这可能是因为数据尚未下载完成")
    
    # 3. 创建和训练模型
    print("\n3. 创建和训练简单的预测模型...")
    try:
        # 创建模型和数据集
        model = init_instance_by_config(CSI300_GBDT_TASK["model"])
        dataset = init_instance_by_config(CSI300_GBDT_TASK["dataset"])
        
        print("   ✓ 模型和数据集创建成功！")
        print(f"   模型类型: {type(model).__name__}")
        print(f"   数据集类型: {type(dataset).__name__}")
        
        # 展示数据集样例
        print("   数据集样例:")
        example_df = dataset.prepare("train")
        print(f"   训练数据形状: {example_df.shape}")
        print("   特征列（前10个）:")
        print(f"   {example_df.columns[:10].tolist()}")
        
        # 训练模型
        print("   正在训练模型...")
        model.fit(dataset)
        print("   ✓ 模型训练完成！")
        
        # 进行预测
        print("   正在进行预测...")
        pred = model.predict(dataset)
        print(f"   预测结果形状: {pred.shape}")
        print("   预测结果样例:")
        print(pred.head())
        
        print("   ✓ 模型预测完成！")
        
    except Exception as e:
        print(f"   ✗ 模型操作失败: {e}")
        print("   这可能是因为数据不完整或模型配置问题")
    
    # 4. 展示配置信息
    print("\n4. Qlib 配置信息:")
    try:
        print(f"   Qlib 版本: {qlib.__version__}")
        print(f"   数据路径: {provider_uri}")
        print(f"   区域设置: {REG_CN}")
        print("   ✓ 配置信息显示完成！")
    except Exception as e:
        print(f"   ✗ 获取配置信息失败: {e}")
    
    print("\n" + "=" * 50)
    print("Qlib 演示完成！")
    print("接下来你可以:")
    print("1. 运行 examples/workflow_by_code.py 查看完整工作流")
    print("2. 使用 qrun 命令运行预定义的策略")
    print("3. 查看 examples/benchmarks/ 目录下的各种模型示例")
    print("=" * 50)

if __name__ == "__main__":
    main()