# Iride 6D → AstroStack 会话读取器

Iride 会在照片目录中为每个观测夜生成一份 CSV 日志（例如 `DCIM/100CANON/IS261102.CSV` 代表 2026 年 11 月 2 日入夜至次日正午的整晚拍摄；1.4.1 及之前版本按小时命名为 `ISmmddhh.CSV`，本工具同时兼容两种格式）。每行记录一张照片的完整信息：类型（LGHT、DARK、FLAT、BIAS）、曝光时间、ISO、光圈、焦距、6D 机身内部温度、电池电量、月光百分比与高度、估算极限星等、快门类型与触发来源（Iride 间隔器或快门线）。

`iride_session.py` 提供以下接口供 AstroStack 调用：

| 函数 | 功能说明 |
|---|---|
| `load_folder(cartella)` | 按文件名索引拍摄元数据（兼容 RAW+JPEG 的 JPEG 文件） |
| `darks_for(light, scatti)` | 为指定亮场匹配同曝光、同 ISO 且温差在 3°C 以内的暗场 |
| `abbina_silenziosi(dng, sessioni)` | 将静音快门拍出的无 EXIF DNG 文件按顺序与 CSV 日志配对 |
| `riepilogo(sessione)` | 输出会话摘要，如 `"IS261102.CSV: 120 LGHT, 30 DARK, 20-24 gradi"` |
| `piano_stack(cartella)` | 自动生成就绪堆栈方案：按曝光/ISO/焦距分组亮场，匹配同温暗场、同焦距平场与同 ISO 偏置场，并给出缺失校准帧提示 |
| `gruppo.migliori(0.9)` | 筛选夜空质量最佳（极限星等最高、月光干扰最小）的前 90% 亮场 |

## 集成到 AstroStack

- **sorter**：检测到会话日志时，直接读取日志中的帧类型，无需依赖文件名猜测。
- **master_library**：对每组亮场调用 `darks_for` 选取温差匹配的暗场。
- **frames_table**：展示温度、月光与极限星等附加列，方便剔除劣质帧。

若目录中无 Iride 日志，AstroStack 仍按原有逻辑工作。

快速命令行测试：`python iride_session.py 照片目录`（附加 `--json` 可输出供 AstroStack 使用的 JSON 堆栈计划）。

### Python 调用示例

```python
from iride_session import piano_stack

for g in piano_stack(cartella):
    lights = [os.path.join(cartella, f.file) for f in g.migliori(0.9)]
    darks = [os.path.join(cartella, f.file) for f in g.dark]
    for a in g.avvisi:
        log.warning(a)              # 例如缺失同焦距平场、暗场张数偏少等提示
    pipeline.stack(lights, darks=darks)
```

使用 Iride 1.6 拍后暗场建议功能拍摄的暗场已自动对齐曝光、ISO 与传感器温度，`piano_stack` 会直接自动匹配。
