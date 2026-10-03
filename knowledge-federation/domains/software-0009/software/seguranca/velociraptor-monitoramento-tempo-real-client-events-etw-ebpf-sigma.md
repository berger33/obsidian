---
id: software.seguranca.tranche03.000296
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://docs.velociraptor.app/docs/overview/", "https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md", "https://github.com/Velocidex/velociraptor"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Velociraptor Detecção em Tempo Real (`CLIENT_EVENT`): monitoramento contínuo via `ETW` (Windows), `eBPF` (Linux) e regras `Sigma`

## Em uma frase
Conforme detalhado na seção *Detecting future attacks* da visão geral oficial (`docs.velociraptor.app/docs/overview/`), além de coletas pontuais sob demanda, o Velociraptor atua como um sensor contínuo de detecção em tempo real através de artefatos do tipo **`CLIENT_EVENT`**, que escutam fontes de eventos ao vivo do sistema operacional — como **Event Tracing for Windows (`ETW` via `watch_etw()`)**, **Windows Event Logs (`watch_evtx()`)**, **Linux `eBPF` (`watch_ebpf()`)** e **`auditd`** — e avaliam **regras `Sigma` (`Windows.Hayabusa.Monitoring` / `Windows.Sigma.Base`)** diretamente no endpoint!

## Por que importa
Encaminhar 100% dos eventos brutos de criação de processos, DNS e PowerShell de 20.000 estações Windows para um SIEM central custa uma fortuna em ingestão de dados.

## Como funciona
No Velociraptor, a query VQL contínua (`CLIENT_EVENT`) e o motor de regras **Sigma** avaliam o stream de eventos **localmente no endpoint com baixíssimo uso de CPU** e transmitem para o servidor Velociraptor apenas os eventos que acionaram uma regra de detecção (ou um resumo deduplicado via `fifo()` / `dedup()`)!

## Exemplo
```sql
-- Exemplo de query VQL contínua (CLIENT_EVENT) monitorando novos processos via eBPF no Linux:
SELECT System.TimeStamp AS Timestamp,
       System.ProcessID AS Pid,
       System.UserID AS Uid,
       EventData.FileName AS Exe,
       EventData.CommandLine AS CommandLine
FROM watch_ebpf(events="sched_process_exec")
WHERE CommandLine =~ "(?i)(base64|curl|wget|nc -e|/dev/tcp/)"
```

## Limites e trade-offs
Os eventos gerados por artefatos `CLIENT_EVENT` ficam armazenados em séries temporais no servidor Velociraptor e podem acionar automaticamente artefatos de resposta do tipo **`SERVER_EVENT`** (por exemplo: colocar o host em quarentena ou coletar um dump forense automaticamente quando uma regra Sigma crítica disparar!).

## Como verificar
Liste os artefatos de monitoramento disponíveis com `velociraptor artifacts list | grep Events`.

## Conexões
- [[velociraptor-offline-collector-triagem-sem-agente-zip-criptografado-s3]] — Veja também: Velociraptor `Offline Collector`: geração de binário autônomo pré-configurado para triagem forense com upload cifrado (`ZIP` / `S3` / `Azure`).
- [[velociraptor-pericia-ntfs-raw-accessor-mft-usnjrnl-vss-virtual-client]] — Veja também: Velociraptor Perícia Forense de Disco (`ntfs`, `raw_ntfs`, `$MFT`, `$UsnJrnl` e Análise de Imagens de Disco via `remapping`).

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://docs.velociraptor.app/docs/overview/) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
