---
id: software.seguranca.tranche13.001212
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

# Extração Forense com **`log2timeline.py`**: Processando Imagens **E01/RAW**, Partições Múltiplas (`--partitions`), **Volume Shadow Copies (`--vss_stores`)** e **BitLocker**

## Em uma frase
Uma das capacidades mais poderosas do **`log2timeline.py`** (construída sobre a suíte de bibliotecas forenses **`dfVFS` — *Digital Forensics Virtual File System*** de Joachim Metz) é ler diretamente **imagens de disco forenses completas (`.E01` EnCase, `.dd`/`.raw`, `.qcow2`, `.vmdk`, `.vhdx`)** sem que você precise montar manualmente as partições no sistema operacional host!

## Por que importa
Quando você aponta o `log2timeline.py` para uma imagem de disco, ele detecta automaticamente a tabela de partições GPT/MBR, identifica volumes criptografados com **BitLocker (`bde`)**, **FileVault (`fvde`)** ou **LUKS (`luksde`)** (permitindo destravá-los passando `--credential recovery_password:...` ou `--credential password:...`) e localiza todas as **Volume Shadow Copies (`VSS`)** do Windows!

## Como funciona
Para automação em lote sem prompts interativos no terminal, utilize sempre as flags **`--partitions all`** (ou `--partitions 2`), **`--vss_stores all`** (que extrai eventos históricos inclusive de arquivos e logs `.evtx` que o atacante apagou na partição ativa, mas que ainda existem dentro dos snapshots VSS!) e **`--unattended`**!

## Exemplo
```bash
# Extrair uma Super Timeline completa de uma imagem E01 incluindo todas as Volume Shadow Copies (VSS) em modo nao-interativo
log2timeline.py \
  --storage-file ./caso_incidente_01.plaso \
  --partitions all \
  --vss_stores all \
  --unattended \
  ./evidencias/servidor_comprometido.E01
```

## Limites e trade-offs
O `log2timeline.py` deduzplica automaticamente registros idênticos encontrados entre a partição ativa e as cópias de sombra (`VSS`), evitando inflar o arquivo `.plaso` com milhões de eventos repetidos.

## Como verificar
Antes de iniciar os processos `Worker_00..Worker_NN`, o estágio **`[PreProcess]`** lê o Registro do Windows ou o `/etc/` do Linux/macOS para descobrir o `hostname`, fuso horário nativo da máquina, versão do SO e variáveis de caminho (`%SystemRoot%`), selecionando automaticamente o **Parser Preset** adequado!

## Conexões
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Veja também: Arquitetura do **Plaso (`log2timeline/plaso`)**: Motor de **Super Timeline Forense** Multi-Artefatos para Windows, Linux, macOS e Android.
- [[plaso-presets-parsers-customizados-win7-linux-macos-targeted-timelines]] — Veja também: Timelines Direcionadas (**Targeted Timelines**) no Plaso: Controlando **`--parsers`** (`win7`, `linux`, `macosx`, `webhist`) e **`-f` Filter Files**.
- [[plaso-inspecao-diagnostico-pinfo-compare-auditoria-extracao]] — Referência cruzada direta com plaso-inspecao-diagnostico-pinfo-compare-auditoria-extracao.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
