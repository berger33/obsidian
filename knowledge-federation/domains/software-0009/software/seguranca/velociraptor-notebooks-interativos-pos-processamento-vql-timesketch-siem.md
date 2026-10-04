---
id: software.seguranca.tranche03.000298
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

# Velociraptor `Notebooks` Colaborativos e Exportação (`Timesketch`, `Splunk`, `Elastic` e `S3`): análise pós-coleta sem reinterrogar o host

## Em uma frase
Conforme destacado na seção *The Velociraptor ecosystem (Analysis & Exports)* de `docs.velociraptor.app/docs/overview/`, toda coleta individual ou *Hunt* no Velociraptor cria automaticamente um **Notebook Interativo** onde múltiplos analistas de resposta a incidentes podem escrever e reexecutar queries VQL de pós-processamento (`source()`) sobre os dados já coletados no servidor!

## Por que importa
Se uma Hunt coletou a lista de 500 processos de cada um dos 5.000 servidores (2,5 milhões de linhas salvas no servidor Velociraptor), você não precisa interrogar os endpoints novamente toda vez que quiser filtrar por um novo hash, agrupar por `CommandLine` (`GROUP BY`) ou enriquecer com Threat Intelligence.

## Como funciona
No Notebook, a função VQL **`source()`** lê os resultados armazenados no servidor em segundos, permite documentar a investigação em células Markdown lado a lado com células VQL e exportar timelines forenses diretamente para o **Google Timesketch (`Server.Utils.TimesketchUpload`)**, **Elastic (`Elastic.Flows.Upload`)**, **Splunk (`Splunk.Flows.Upload`)** ou **AWS S3 (`Server.Utils.BackupS3`)**!

## Exemplo
```sql
-- Exemplo de célula VQL em um Notebook de Hunt: agrupa os processos mais raros encontrados nos endpoints:
SELECT Name, Exe, CommandLine, count() AS HostCount
FROM source(artifact="Windows.System.Pslist")
GROUP BY Exe, CommandLine
ORDER BY HostCount ASC
LIMIT 25
```

## Limites e trade-offs
Essa técnica de *Stack Counting / Least Frequency of Occurrence* (`ORDER BY HostCount ASC`) em um Notebook de Hunt é uma das formas mais eficazes de *Threat Hunting*: serviços legítimos corporativos aparecem em centenas de máquinas, enquanto uma persistência ou backdoor do atacante aparece em apenas 1 ou 2 hosts!

## Como verificar
Explore o Notebook gerado após qualquer coleta na GUI do Velociraptor e edite a célula VQL padrão.

## Conexões
- [[velociraptor-pericia-ntfs-raw-accessor-mft-usnjrnl-vss-virtual-client]] — Veja também: Velociraptor Perícia Forense de Disco (`ntfs`, `raw_ntfs`, `$MFT`, `$UsnJrnl` e Análise de Imagens de Disco via `remapping`).
- [[velociraptor-orquestracao-ferramentas-externas-thor-hayabusa-cybertriage-quarantine]] — Veja também: Velociraptor Orquestração de Ferramentas de Terceiros (`Tools`) e Resposta Ativa (`Windows.Remediation.Quarantine`).

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://docs.velociraptor.app/docs/overview/) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
