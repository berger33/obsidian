---
id: software.seguranca.tranche13.001213
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

# Timelines Direcionadas (**Targeted Timelines**) no Plaso: Controlando **`--parsers`** (`win7`, `linux`, `macosx`, `webhist`) e **`-f` Filter Files**

## Em uma frase
Processar 100% dos arquivos de um disco de 2 TB para gerar uma Super Timeline completa pode levar horas. E quando você está nos primeiros 30 minutos de uma resposta a incidentes crítica e precisa gerar uma **Targeted Timeline (*Timeline Direcionada*)** em apenas 3 minutos contendo exclusivamente artefatos de execução, logs de eventos, registro e histórico de navegadores?

## Por que importa
O `log2timeline.py` oferece dois mecanismos de aceleração cirúrgica: **(1) A flag `--parsers`**, que aceita nomes de *presets* (`win7`, `win_gen`, `linux`, `macosx`, `android`, `webhist`) e operadores de inclusão/exclusão (ex.: `--parsers "win7,!filestat"` para rodar todos os parsers forenses do Windows excluindo o parser genérico de metadados de todos os arquivos do disco, ou `--parsers "winevtx,winreg,prefetch,lnk,mft"` para extrair apenas os artefatos principais!); e **(2) A flag `-f, --file-filter`**, que recebe um arquivo YAML ou texto listando apenas os caminhos de arquivos do disco que o `dfVFS` deve abrir!

## Como funciona
Combinando `-f filtro_artefatos.yaml` com `--parsers`, o `log2timeline.py` salta diretamente para os inodes dos artefatos críticos na imagem `.E01` e conclui a extração em poucos minutos!

## Exemplo
```bash
# Gerar uma Targeted Timeline ultrarrapida focada apenas em Event Logs, Registro, Prefetch, LNK e Historico Web
log2timeline.py \
  --storage-file ./triagem_rapida_win.plaso \
  --parsers "winevtx,winreg,prefetch,lnk,webhist" \
  --unattended \
  ./evidencias/estacao_paciente_zero.E01
```

## Limites e trade-offs
Para usar as definições padronizadas do repositório **ForensicArtifacts (`artifacts`)**, passe **`--artifact-filters WindowsTriageEvents`** ao `log2timeline.py`: ele utilizará o catálogo YAML oficial de artefatos forenses em `/usr/share/artifacts/` para coletar exatamente os caminhos relevantes de cada sistema operacional!

## Como verificar
Lembre-se da sintaxe hierárquica do Plaso ao especificar plugins filhos em `--parsers`: um plugin de banco SQLite ou registro deve ser prefixado pelo seu parser pai (ex.: `sqlite/chrome_history`, `winreg/appcompatcache`, `text/winiis`).

## Conexões
- [[plaso-extracao-imagens-disco-log2timeline-particoes-vss-bitlocker]] — Veja também: Extração Forense com **`log2timeline.py`**: Processando Imagens **E01/RAW**, Partições Múltiplas (`--partitions`), **Volume Shadow Copies (`--vss_stores`)** e **BitLocker**.
- [[plaso-inspecao-diagnostico-pinfo-compare-auditoria-extracao]] — Veja também: Auditoria e Diagnóstico de Arquivos `.plaso` com **`pinfo.py`**: Metadados de Pré-Processamento, Contagem por Parser e **`--compare`**.
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Referência cruzada direta com plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite.
- [[chainsaw-analise-shimcache-amcache-timeline-execucao-binarios]] — Referência cruzada direta com chainsaw-analise-shimcache-amcache-timeline-execucao-binarios.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
