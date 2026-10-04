---
id: software.seguranca.tranche13.001214
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

# Auditoria e Diagnóstico de Arquivos `.plaso` com **`pinfo.py`**: Metadados de Pré-Processamento, Contagem por Parser e **`--compare`**

## Em uma frase
Antes de começar a analisar uma Super Timeline no `psort.py` ou no Timesketch, todo perito forense deve executar o utilitário **`pinfo.py`** sobre o arquivo `.plaso` gerado! Por quê?

## Por que importa
Porque o **`pinfo.py`** exibe a "radiografia" completa da extração forense realizada pelo `log2timeline.py`: **(1) Atributos descobertos no `[PreProcess]`** (`hostname`, `os_version`, `time_zone`, contas de usuários locais e seus SIDs/UIDs, variáveis de ambiente do sistema); **(2) Parâmetros exatos da sessão** (versão do Plaso, linha de comando usada, parsers habilitados); **(3) Tabela de contagem de eventos extraídos por cada parser individual** (ex.: quantos eventos vieram do `winevtx`, quantos do `mft`, quantos do `filestat`, quantos do `sqlite/chrome_27_history`); e **(4) Relatório de `Warnings` / `Recovery`** (arquivos corrompidos ou truncados que falharam no parse)!

## Como funciona
Além disso, o `pinfo.py` possui a flag **`--compare outro_arquivo.plaso`**, que compara dois arquivos `.plaso` e verifica se eles contêm exatamente os mesmos eventos e metadados!

## Exemplo
```bash
# Inspecionar o resumo executivo, atributos de sistema extraidos e estatisticas de eventos por parser de um arquivo .plaso
pinfo.py ./caso_incidente_01.plaso
pinfo.py --sections events,warnings ./caso_incidente_01.plaso
```

## Limites e trade-offs
Use a flag **`--sections`** do `pinfo.py` (`sessions`, `sources`, `system`, `events`, `warnings`, `reports`, `tags`) para gerar relatórios enxutos que podem ser anexados diretamente ao Laudo Pericial da investigação.

## Como verificar
Se a tabela `events` do `pinfo.py` mostrar `0` eventos para um parser esperado (por exemplo, `winevtx = 0` em um servidor Windows), isso alerta imediatamente o perito de que a partição selecionada estava incorreta ou que os arquivos `.evtx` foram apagados do sistema de arquivos ativo.

## Conexões
- [[plaso-presets-parsers-customizados-win7-linux-macos-targeted-timelines]] — Veja também: Timelines Direcionadas (**Targeted Timelines**) no Plaso: Controlando **`--parsers`** (`win7`, `linux`, `macosx`, `webhist`) e **`-f` Filter Files**.
- [[plaso-filtragem-exportacao-psort-time-slice-dynamic-output-l2tcsv]] — Veja também: Pós-Processamento, Recorte Temporal (**`--slice`**) e Linguagem de Filtro no **`psort.py`**: Exportando `l2tcsv`, `dynamic` e `json_line`.
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Referência cruzada direta com plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite.
- [[plaso-extracao-imagens-disco-log2timeline-particoes-vss-bitlocker]] — Referência cruzada direta com plaso-extracao-imagens-disco-log2timeline-particoes-vss-bitlocker.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
