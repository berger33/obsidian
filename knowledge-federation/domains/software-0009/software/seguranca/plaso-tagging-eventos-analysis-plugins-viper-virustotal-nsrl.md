---
id: software.seguranca.tranche13.001216
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/log2timeline/plaso/main/README.md", "https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Rotulagem Automática (**Event Tagging**) e **Analysis Plugins** no Plaso: Destacando Execução, Persistência, Logins e Indicadores Maliciosos

## Em uma frase
Como encontrar automaticamente a "agulha no palheiro" dentro de um arquivo `.plaso` com 3 milhões de eventos antes mesmo de abrir a planilha CSV ou o Timesketch?

## Por que importa
O Plaso possui um motor nativo de **Rotulagem Automática de Eventos (*Event Tagging*)** e **Analysis Plugins** executados pelo `psort.py`: usando a flag **`--tagging-file`** (ou os arquivos de regras de tag padrão por sistema operacional como `tag_windows.txt` e `tag_linux.txt`), o Plaso avalia condições lógicas sobre cada evento e aplica **Tags Semânticas** como **`application_execution`** (Prefetch, Shimcache, Amcache, UserAssist, LNK), **`autorun`** (chaves Run/Services, Cron, Systemd), **`logon`** / **`logoff`**, **`file_download`**, **`device_connection`** (USB) e **`eventlog_cleared`**!

## Como funciona
Além das tags, os **Analysis Plugins** (`--analysis`) analisam o conjunto de eventos para extrair estatísticas de contas de navegador (`browser_search`), extensões do Chrome (`chrome_extension`), serviços e tarefas agendadas do Windows (`windows_services`) e consultar hashes `sha256` contra listas de referência (**`nsrlsvr`**, **`virustotal`**, **`viper`**)!

## Exemplo
```bash
# Aplicar o plugin de analise de Tagging automatico do Windows em um arquivo .plaso e exportar apenas eventos rotulados com tags criticas
psort.py \
  --analysis tagging \
  --tagging-file /usr/share/plaso/tag_windows.txt \
  -o dynamic \
  -w ./eventos_rotulados_criticos.csv \
  ./caso_incidente_01.plaso \
  "tag is not None"
```

## Limites e trade-offs
Olhe a potência do filtro final **`"tag is not None"`** no comando `psort.py` acima: depois de rodar `--analysis tagging`, o arquivo `.plaso` grava os rótulos de cada evento, e filtrar por `"tag is not None"` (ou `"tag contains 'application_execution'"`) reduz instantaneamente milhões de eventos brutos para apenas os milhares de eventos de alta relevância forense!

## Como verificar
Você pode criar seu próprio arquivo `tag_custom_dfir.txt` adicionando regras para rotular IPs de C2, contas comprometidas ou ferramentas de exfiltração específicas do caso.

## Conexões
- [[plaso-filtragem-exportacao-psort-time-slice-dynamic-output-l2tcsv]] — Veja também: Pós-Processamento, Recorte Temporal (**`--slice`**) e Linguagem de Filtro no **`psort.py`**: Exportando `l2tcsv`, `dynamic` e `json_line`.
- [[plaso-integracao-timesketch-opensearch-psteal-investigacao-colaborativa]] — Veja também: Pipeline Direto **`psteal.py`** e Integração Nativa **Plaso + Google Timesketch (`opensearch_ts`)**: Investigação Forense Colaborativa em Escala.
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Referência cruzada direta com plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
