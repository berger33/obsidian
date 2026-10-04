---
id: software.seguranca.tranche13.001211
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

# Arquitetura do **Plaso (`log2timeline/plaso`)**: Motor de **Super Timeline Forense** Multi-Artefatos para Windows, Linux, macOS e Android

## Em uma frase
Enquanto ferramentas como **Hayabusa** e **Chainsaw** focam em triagem rápida de artefatos específicos do Windows, como um perito de **DFIR (*Digital Forensics and Incident Response*)** reconstrói uma **Super Timeline cronológica unificada ("Super Timeline all the things")** que correlaciona, segundo a segundo, **todos os eventos de um disco inteiro** — desde um download no navegador Chrome/Firefox, a criação do arquivo na `$MFT`/ext4, a execução no Prefetch/Shimcache/Syslog, a modificação no Registro/plist até a conexão SSH/RDP?

## Por que importa
Criado originalmente por Kristinn Gudjonsson e mantido pelo projeto open-source **log2timeline / Google DFIR**, o **Plaso** é o motor padrão mundial de geração de Super Timelines forenses!

## Como funciona
Sua arquitetura é composta por quatro ferramentas de linha de comando que operam sobre um contêiner intermediário `.plaso` (baseado em SQLite): **(1) `log2timeline.py`** (extrai eventos de imagens de disco `.E01`/`.dd`/`.vmdk`, Volume Shadow Copies `VSS` ou diretórios montados usando centenas de parsers e múltiplos processos `Worker_XX`); **(2) `pinfo.py`** (inspeciona metadados, contagens de eventos por parser e erros do arquivo `.plaso`); **(3) `psort.py`** (filtra por janela temporal, executa plugins de análise e exporta para CSV, JSONL ou **OpenSearch/Timesketch**); e **(4) `psteal.py`** (que encadeia `log2timeline` + `psort` em um único comando)!

## Exemplo
```bash
# Listar todos os presets de sistema operacional, parsers, plugins e formatos de saida suportados pela instalacao do Plaso
log2timeline.py --info
```

## Limites e trade-offs
Por que o Plaso separa a fase de extração (`log2timeline.py` -> `.plaso`) da fase de filtragem e exportação (`psort.py`)? Porque processar uma imagem forense de 500 GB pode extrair milhões de eventos; uma vez gravados no arquivo estruturado `.plaso`, você pode rodar o `psort.py` dezenas de vezes com recortes temporais e filtros diferentes sem precisar reprocessar a imagem de disco!

## Como verificar
Execute o Plaso a partir da imagem Docker oficial (`log2timeline/plaso`) ou pacote GIFT PPA para ter todas as bibliotecas C de sistemas de arquivos (`libewf`, `libfsntfs`, `libfsext`, `libvshadow`, `libbde`) pré-compiladas.

## Conexões
- [[plaso-extracao-imagens-disco-log2timeline-particoes-vss-bitlocker]] — Veja também: Extração Forense com **`log2timeline.py`**: Processando Imagens **E01/RAW**, Partições Múltiplas (`--partitions`), **Volume Shadow Copies (`--vss_stores`)** e **BitLocker**.
- [[plaso-filtragem-exportacao-psort-time-slice-dynamic-output-l2tcsv]] — Referência cruzada direta com plaso-filtragem-exportacao-psort-time-slice-dynamic-output-l2tcsv.
- [[chainsaw-workflow-integrado-chainsaw-hayabusa-kape-velociraptor-dfir]] — Referência cruzada direta com chainsaw-workflow-integrado-chainsaw-hayabusa-kape-velociraptor-dfir.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
