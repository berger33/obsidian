---
id: software.seguranca.tranche03.000291
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
fontes: ["https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md", "https://docs.velociraptor.app/docs/overview/", "https://github.com/Velocidex/velociraptor"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Rapid7 Velociraptor: arquitetura da plataforma open-source de `DFIR` e visibilidade de endpoints movida por `VQL`

## Em uma frase
Conforme documentado no README oficial (`Velocidex/velociraptor`, escrito em Go) e na visão geral oficial (`docs.velociraptor.app/docs/overview/`), o **Velociraptor** é uma plataforma empresarial open-source para **monitoramento de endpoints, perícia digital (*Digital Forensics*) e resposta a incidentes (*Incident Response — DFIR*)** em Windows, Linux e macOS, cujo poder vem da linguagem **VQL (*Velociraptor Query Language*)**.

## Por que importa
Como explica a seção *The incident response timeline* da documentação oficial, um incidente envolve três tempos: **1. O ataque inicial no passado** (exigindo perícia forense profunda em disco/NTFS/MFT/EventLogs/Registry), **2. O tempo presente da resposta** (exigindo triagem rápida e *Hunting* em milhares de máquinas) e **3. Ataques futuros** (exigindo monitoramento em tempo real via `ETW`, `eBPF` e regras `Sigma`).

## Como funciona
Um **único binário estático em Go** (`velociraptor`) atua tanto como o **Servidor** (`frontend`, `gui`), quanto como o **Agente de Endpoint (`client`)** conectado via canal persistente mTLS, ou como um **Coletor Offline standalone**!

## Exemplo
```bash
# Iniciando um ambiente completo de avaliação do Velociraptor (GUI + Frontend + Client local) com um único comando:
velociraptor gui
```

## Limites e trade-offs
Consulte sempre a página oficial de downloads e avisos de segurança (`docs.velociraptor.app/announcements/advisories/`) para manter o binário do servidor e dos clientes atualizado na última versão estável.

## Como verificar
Execute `velociraptor version` para verificar a versão, o commit e os recursos compilados no binário.

## Conexões
- [[velociraptor-vql-velociraptor-query-language-plugins-functions-foreach]] — Veja também: Velociraptor Query Language (`VQL`): consultas reativas com plugins geradores de linhas (`pslist`, `glob`, `parse_mft`, `yara`) e `foreach()`.

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://docs.velociraptor.app/docs/overview/) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
