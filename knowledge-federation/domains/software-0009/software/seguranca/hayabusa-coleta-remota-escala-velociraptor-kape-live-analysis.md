---
id: software.seguranca.tranche11.001096
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md", "https://yamato-security.github.io/hayabusa/commands/", "https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Caça a Ameaças em Escala Corporativa: Integrando **Hayabusa** com **Rapid7 Velociraptor** e **KAPE** + Execução **`--live-analysis`**

## Em uma frase
Como executar o Hayabusa contra **5.000 estações Windows e servidores Active Directory simultaneamente** durante um incidente crítico sem precisar copiar terabytes de arquivos `.evtx` brutos pela rede da empresa?

## Por que importa
Existem duas arquiteturas consagradas documentadas pelo projeto Hayabusa: **(1) Execução Distribuída no Endpoint via Velociraptor (`Windows.Hayabusa.Rules` / Artifact)** — o agente do **Velociraptor** distribui o binário compilado do `hayabusa.exe` (junto com o pacote de regras embutido ou zipado) para cada endpoint Windows, executa `hayabusa json-timeline --live-analysis` localmente usando a CPU de cada máquina em poucos segundos e **envia de volta para o servidor Velociraptor apenas os alertas JSONL detectados (`medium`/`high`/`critical`)**!;

## Como funciona
ou **(2) Coleta Centralizada de Artefatos (`.evtx`) via Velociraptor (`Windows.KapeFiles.Targets`) / KAPE** seguida de processamento em lote (`hayabusa csv-timeline -d /colecao_central/`) no servidor forense!

## Exemplo
```bash
# Em um sistema Windows ao vivo (com privilegios de Administrador): analisar diretamente os canais de Event Log ativos (--live-analysis)
hayabusa csv-timeline \
  --live-analysis \
  --min-level medium \
  --output C:\Temp\hayabusa_live_triage.csv
```

## Limites e trade-offs
Quando usar a **Abordagem 1 (Executar Hayabusa no Endpoint via Velociraptor)** vs a **Abordagem 2 (Coletar `.evtx` para o Servidor Forense)**? Use a **Abordagem 1** para *Triage & Threat Hunting Rápido* em milhares de máquinas (para descobrir em 5 minutos *quais* das 5.000 máquinas foram tocadas pelo atacante!), e imediatamente aplique a **Abordagem 2** (coleta forense completa de `.evtx`, MFT, Registry e Memória) nas máquinas que apresentarem alertas positivos!

## Como verificar
Isso economiza 99% de tráfego de rede e entrega visibilidade corporativa em minutos.

## Conexões
- [[hayabusa-calibracao-regras-level-tuning-expand-list-custom-rules]] — Veja também: Calibração de Severidade e Regras no Hayabusa: **`level-tuning`**, **`expand-list`**, Perfis de Status (`--status`) e Regras Sigma Customizadas (`--rules`).
- [[hayabusa-canais-evtx-essenciais-sysmon-powershell-rdp-defender-wmi]] — Veja também: Os **10 Canais de Log Windows (`.evtx`) Mais Valiosos** Analisados pelo Hayabusa: Muito Além de `Security.evtx`, `System.evtx` e `Application.evtx`.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.
- [[velociraptor-arquitetura-dfir-endpoint-visibility-vql-client-server]] — Referência cruzada direta com velociraptor-arquitetura-dfir-endpoint-visibility-vql-client-server.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
