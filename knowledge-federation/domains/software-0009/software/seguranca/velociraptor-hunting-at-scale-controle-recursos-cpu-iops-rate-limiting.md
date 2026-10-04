---
id: software.seguranca.tranche03.000294
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

# Velociraptor `Hunts` em Escala e Controle de Recursos no Endpoint: `ops_per_second`, limite de CPU (`max_cpu`) e `timeout`

## Em uma frase
Conforme destacado em `docs.velociraptor.app/docs/overview/` (*"By scaling triage analysis to the entire environment — Hunting the environment — we are able to zero in on compromised assets quickly... using Velociraptor's sophisticated control of endpoint resource usage"*), uma **Hunt** agenda a coleta de um ou mais *Artifacts* em milhares de endpoints filtrados por labels ou sistema operacional.

## Por que importa
Se você disparar uma varredura YARA ou de disco em 15.000 servidores de produção ao mesmo tempo sem limitador de CPU e I/O, o pico de leitura de disco pode degradar bancos de dados críticos.

## Como funciona
Ao criar uma coleta ou *Hunt* no Velociraptor, você define limites estritos de recursos aplicados pelo próprio agente no endpoint: **Limite de CPU (`CpuLimit`, percentual máximo de CPU via token bucket no avaliador VQL)**, **Taxa de IOPS (`OpsPerSecond`)**, **`Timeout` máximo de execução** e **Limite de bytes/linhas transferidos (`MaxRow`, `MaxUploadBytes`)**!

## Exemplo
```bash
# Executando um artefato localmente com limite máximo de 20% de utilização de CPU e timeout de 120 segundos:
velociraptor artifacts collect Generic.Client.Info \
  --cpu_limit 20 \
  --timeout 120
```

## Limites e trade-offs
Ao lançar uma nova *Hunt* para toda a frota, defina primeiro um limite de máquinas (`Client Limit = 50`) como grupo piloto, verifique nos gráficos da aba *Notebook / Stats* da Hunt o tempo médio de CPU e o volume de dados coletados por host, e só então expanda o limite para o restante da frota!

## Como verificar
Inspecione o log de execução (`Query Stats`) de uma coleta na GUI para auditar a duração e a memória consumida no cliente.

## Conexões
- [[velociraptor-artifacts-yaml-client-server-events-artifact-exchange]] — Veja também: Velociraptor `Artifacts` e `Artifact Exchange`: empacotamento YAML de queries VQL (`CLIENT`, `SERVER`, `CLIENT_EVENT`, `SERVER_EVENT`).
- [[velociraptor-offline-collector-triagem-sem-agente-zip-criptografado-s3]] — Veja também: Velociraptor `Offline Collector`: geração de binário autônomo pré-configurado para triagem forense com upload cifrado (`ZIP` / `S3` / `Azure`).

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://docs.velociraptor.app/docs/overview/) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
