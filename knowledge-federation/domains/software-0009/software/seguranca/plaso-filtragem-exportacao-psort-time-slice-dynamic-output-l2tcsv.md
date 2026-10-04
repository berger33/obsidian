---
id: software.seguranca.tranche13.001215
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

# Pós-Processamento, Recorte Temporal (**`--slice`**) e Linguagem de Filtro no **`psort.py`**: Exportando `l2tcsv`, `dynamic` e `json_line`

## Em uma frase
Uma Super Timeline completa de um servidor ativo pode conter de **1 milhão a 10 milhões de eventos** cobrindo anos de histórico do sistema operacional. Como usar o **`psort.py`** para recortar apenas a janela exata do incidente ou os 15 minutos ao redor de um alerta de EDR (**Time Slicing**)?

## Por que importa
O **`psort.py`** possui dois mecanismos de filtragem de altíssima precisão: **(1) Linguagem de Expressão de Filtro** (passada como argumento final, ex.: `date > '2026-10-01 00:00:00' AND date < '2026-10-03 23:59:59'` ou `parser is 'winevtx' AND message iregexp 'mimikatz|rclone'`); e **(2) Time Slice (`--slice <timestamp>` e `--slice_size <minutos>`)** — uma função brilhante para resposta a incidentes: se o seu EDR alertou sobre uma execução suspeita às `2026-10-02T14:32:10`, passar `--slice "2026-10-02T14:32:10" --slice_size 5` extrai automaticamente **todos os eventos de todos os artefatos do disco que ocorreram exatamente nos 5 minutos antes e nos 5 minutos depois daquele segundo crítico**!

## Como funciona
Na saída (`-o`), você pode escolher entre **`l2tcsv`** (o formato clássico de 17 colunas do `log2timeline`), **`dynamic`** (onde você escolhe exatamente quais colunas quer no CSV via `--fields`) ou **`json_line`** (para ingestão em SIEM/Timesketch)!

## Exemplo
```bash
# Extrair com psort.py uma fatia temporal (--slice) de 10 minutos ao redor do horario exato de um alerta de intrusao em formato CSV dinamico
psort.py \
  -o dynamic \
  --fields datetime,timestamp_desc,source,source_long,message,filename \
  --output_time_zone "America/Sao_Paulo" \
  --slice "2026-10-02T14:32:10" \
  --slice_size 10 \
  -w ./fatia_incidente_1432.csv \
  ./caso_incidente_01.plaso
```

## Limites e trade-offs
A flag **`--output_time_zone`** no `psort.py` converte todos os timestamps (que o Plaso armazena internamente sempre normalizados em **UTC**) para o fuso horário desejado no momento da exportação, sem alterar o arquivo `.plaso` original.

## Como verificar
Use `-a` (*include all*) apenas quando quiser desativar a deduplicação automática de eventos idênticos na saída do `psort.py`.

## Conexões
- [[plaso-inspecao-diagnostico-pinfo-compare-auditoria-extracao]] — Veja também: Auditoria e Diagnóstico de Arquivos `.plaso` com **`pinfo.py`**: Metadados de Pré-Processamento, Contagem por Parser e **`--compare`**.
- [[plaso-tagging-eventos-analysis-plugins-viper-virustotal-nsrl]] — Veja também: Rotulagem Automática (**Event Tagging**) e **Analysis Plugins** no Plaso: Destacando Execução, Persistência, Logins e Indicadores Maliciosos.
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Referência cruzada direta com plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
