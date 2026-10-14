# CV / NVS / 超分辨率 / 图像复原专项审查

仅在论文涉及 **SR, Real-ISR, restoration, RAW/sRGB, diffusion/flow, view synthesis, ISP** 等任务时加载；不要把下列项机械套到所有论文。

## 任务与输入分布

- 明确输入/输出：`RAW→RAW`、`RAW→sRGB`、`sRGB→sRGB`，还是其他混合管线？是否能得到 sensor RAW，还是仅有渲染好的相片？
- LR 生成机制与最终使用场景一致吗？合成 LR 来自 bicubic、传统 blur/noise/JPEG，还是传感器/镜头/ISP 特定 camera pipeline？是否包含真实相机中的 demosaicing、denoise、sharpening、tone/gamma、compression？
- 是否把“降采样后的真值”当作可观测真实 LR？两者的颜色处理、曝光、运动模糊、对齐和细节统计可能不同。
- 成对图像的几何/像素对齐是否成立？高分辨率真值是否包含真实可恢复的信号？数据采集是否引入场景泄漏？

## 模型与学习机制

- backbone、参数量、训练阶段、冻结模块、预训练数据、teacher 与 student、distillation objective 是否区分清楚？
- 对 diffusion / flow / MeanFlow / consistency，确认 forward/noising process、求解器步数、训练目标、条件输入、guidance、随机性、采样预算；推理步数更少不代表整体更快。
- 一致的 loss 定义和权重；L1 / L2 / LPIPS / adversarial / distribution loss 的质量-保真权衡；对 hallucination、纹理与字符/人脸真实性的副作用。
- 对 NVS，检验摄像机位姿、几何尺度、遮挡、视角变化、跨帧稳定、视频连贯性、训练和评价视角是否公平。

## 图表、指标与结果

- 测试集具体采样、×2/×4 缩放、图像大小、RGB/YCbCr、Y 通道或 RGB、裁边策略、是否统一后处理。
- PSNR/SSIM 与 LPIPS/FID/NIQE/MUSIQ 等各自衡量什么？参考/无参考指标的可信程度；跨指标不能直接互证。
- 视觉 zoom crops 是否相同位置、比例、对齐、压缩与曝光？是否精选样例？能否访问完整图、失败案例和主观评价协议？
- 实拍与合成域分别报告；不同 sensor、ISP、照明/ISO、景深/运动、JPEG 压缩级别下是否泛化？
- baseline 的训练数据、感知先验、算力预算、分辨率与推理次数是否等价？所谓更好的 teacher/student 是否比较同一设置？
- 效率：端到端 latency、GPU 型号、batch、模型加载、编码解码、峰值 VRAM、稳定性与重复次数；不从理论 FLOPs 直接推断真实运行时间。

## 将结果转化为高价值研究卡的方向

优先考虑能区分两个解释的最小实验，比如：
- 质量提升来自**更贴近真实 camera pipeline**，还是来自训练集扩充？固定模型与 HR 内容，只切换 degradation；在不同传感器真实 LR 上评估。
- 感知指标收益来自更真实细节还是**幻觉**？固定感知评价，同时追加局部真实性/人评/困难纹理检查。
- 学生超越教师是**损失函数/蒸馏训练/模型规模/测试设置**的哪一部分？做 matched-budget、same-data、same-inference-protocol 的隔离对照。
- 算法收益是否跨 sensor/ISP/放大倍率保持？设置明确的外部测试集和 domain shift 失败门槛。

这些只是 `[R]` 候选问题，**不能在没有纸面证据或实验数据时写成结论**。
