---
id: software.seguranca.tranche13.001217
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

# Pipeline Direto **`psteal.py`** e Integração Nativa **Plaso + Google Timesketch (`opensearch_ts`)**: Investigação Forense Colaborativa em Escala

## Em uma frase
Quando uma equipe de resposta a incidentes precisa analisar simultaneamente Super Timelines de 15 servidores e estações comprometidas em um ataque corporativo, abrir arquivos CSV de 2 GB no Excel é inviável. Qual é a arquitetura padrão criada pelo time de DFIR do Google para esse cenário?

## Por que importa
A combinação nativa entre **Plaso (`log2timeline` / `psteal`)** e **Google Timesketch** (apoiado por **OpenSearch**)!

## Como funciona
Por um lado, se você quer ir diretamente da imagem de disco (`.E01` ou pasta coletada pelo KAPE) para o arquivo de saída em um único passo sem gerenciar manualmente o `.plaso`, o utilitário **`psteal.py`** executa o `log2timeline` e o `psort` encadeados automaticamente! Por outro lado, usando o módulo de saída **`-o opensearch_ts`** do `psort.py` ou o **`timesketch_importer`**, o arquivo `.plaso` (com todos os seus atributos JSON estruturados, tags do Plaso e metadados de pré-processamento) é indexado diretamente em um *Sketch* do **Timesketch**, onde múltiplos peritos podem pesquisar, cruzar linhas do tempo de vários hosts e rodar os *Timesketch Analyzers* (incluindo Sigma!) em paralelo!

## Exemplo
```bash
# Executar extracao + ordenacao em um unico comando com psteal.py ou enviar um arquivo .plaso para o Timesketch via timesketch_importer
psteal.py \
  --source ./coleta_kape_host01/ \
  -o json_line \
  -w ./timeline_host01.jsonl \
  --storage-file ./host01.plaso
```

## Limites e trade-offs
Por que importar o arquivo **`.plaso` (ou `.jsonl` gerado pelo Plaso)** no Timesketch é muito mais rico do que importar um CSV comum? Porque o CSV achata todos os campos específicos do evento dentro de uma única coluna de texto `message`, enquanto o `.plaso` / `json_line` preserva cada atributo individual (`event_identifier`, `xml_string`, `regvalue`, `sha256_hash`, `url`) como um campo indexado e pesquisável no OpenSearch!

## Como verificar
Sempre preserve o arquivo `.plaso` original no armazenamento de evidências do caso mesmo após exportá-lo para o Timesketch.

## Conexões
- [[plaso-tagging-eventos-analysis-plugins-viper-virustotal-nsrl]] — Veja também: Rotulagem Automática (**Event Tagging**) e **Analysis Plugins** no Plaso: Destacando Execução, Persistência, Logins e Indicadores Maliciosos.
- [[plaso-forense-linux-macos-containers-syslog-auditd-plist-unified-logs]] — Veja também: Forense de Servidores **Linux, macOS e Containers** com o Plaso: Parsers `syslog`, `systemd_journal`, `utmp`/`wtmp`, `bash_history`, `fsext` e `plist`.
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Referência cruzada direta com plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite.
- [[plaso-filtragem-exportacao-psort-time-slice-dynamic-output-l2tcsv]] — Referência cruzada direta com plaso-filtragem-exportacao-psort-time-slice-dynamic-output-l2tcsv.
- [[hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch]] — Referência cruzada direta com hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
