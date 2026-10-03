---
id: software.seguranca.tranche03.000293
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

# Velociraptor `Artifacts` e `Artifact Exchange`: empacotamento YAML de queries VQL (`CLIENT`, `SERVER`, `CLIENT_EVENT`, `SERVER_EVENT`)

## Em uma frase
Conforme documentado no README oficial (*Artifact Exchange*) e em `docs.velociraptor.app/docs/overview/`, todo o conhecimento forense do Velociraptor é empacotado em **VQL Artifacts** — arquivos YAML declarativos que encapsulam queries VQL com parâmetros tipados (`parameters`), pré-condições de sistema operacional (`precondition`) e documentação, divididos em quatro tipos: **`CLIENT`**, **`CLIENT_EVENT`**, **`SERVER`** e **`SERVER_EVENT`**.

## Por que importa
Pedir para analistas Júnior do SOC escreverem queries VQL complexas de parsing da `$MFT` ou dos logs `evtx` durante uma crise às 3h da manhã é propenso a erro; com *Artifacts*, o analista apenas seleciona p.ex. `Windows.EventLogs.EvtxHunter` ou `Linux.Sys.Users` na GUI, preenche um parâmetro de busca e clica em *Launch*!

## Como funciona
Além das centenas de artefatos embutidos no binário, a comunidade mantém o catálogo público **[Velociraptor Artifact Exchange](https://docs.velociraptor.app/exchange/)**, que pode ser importado no servidor com um único clique (`Server.Import.ArtifactExchange`)!

## Exemplo
```yaml
name: Custom.Linux.DetectDeletedRunningBinaries
description: Identifica processos Linux em execução cujo binário foi removido do disco.
type: CLIENT
precondition: SELECT OS From info() where OS = 'linux'
parameters:
  - name: ExcludeRegex
    default: "^/dev/shm/"
sources:
  - query: |
      SELECT Pid, Name, Exe, CommandLine, WorkingDirectory
      FROM pslist()
      WHERE Exe =~ "\\(deleted\\)$"
        AND NOT Exe =~ ExcludeRegex
```

## Limites e trade-offs
Teste qualquer arquivo de artefato YAML localmente pela linha de comando usando **`velociraptor artifacts collect Custom.Linux.DetectDeletedRunningBinaries --definitions ./meus-artefatos/`**.

## Como verificar
Liste todos os artefatos embutidos no seu binário executando `velociraptor artifacts list`.

## Conexões
- [[velociraptor-vql-velociraptor-query-language-plugins-functions-foreach]] — Veja também: Velociraptor Query Language (`VQL`): consultas reativas com plugins geradores de linhas (`pslist`, `glob`, `parse_mft`, `yara`) e `foreach()`.
- [[velociraptor-hunting-at-scale-controle-recursos-cpu-iops-rate-limiting]] — Veja também: Velociraptor `Hunts` em Escala e Controle de Recursos no Endpoint: `ops_per_second`, limite de CPU (`max_cpu`) e `timeout`.

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://docs.velociraptor.app/docs/overview/) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
