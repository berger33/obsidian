---
id: software.seguranca.tranche06.000531
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md", "https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md", "https://www.volatilityfoundation.org/license/vsl-v1.0"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Volatility 3: Arquitetura de Análise Forense de Memória RAM, *Intermediate Symbol Format* (`ISF`) e *Translation Layers*

## Em uma frase
**Volatility 3** (`volatilityfoundation/volatility3`, Python 3.8+, licenciado sob VSL) é a reescrita completa do framework padrão mundial para extração e análise forense de artefatos de amostras de memória volátil (RAM) de sistemas Windows, Linux e macOS.

## Por que importa
Muitas ameaças modernas (*fileless malware*, *reflective DLL injection*, *process hollowing*, *cobalt strike beacons* em memória, chaves de criptografia de disco BitLocker/LUKS e conexões de rede ativas) nunca tocam o disco rígido ou apagam seus rastros em arquivo, mas são incapazes de se esconder na memória RAM física enquanto executam.

## Como funciona
Diferente do antigo Volatility 2 (que usava *profiles* rígidos), o Volatility 3 separa a tradução de endereços físicos/virtuais (*Translation Layers*: Intel 32/64-bit paging, Windows Crash Dump, LiME, VMware `.vmem`, QEMU/ELF) das **Symbol Tables** em formato JSON padronizado (**ISF** — *Intermediate Symbol Format*), organizando os plugins por namespace (`windows.*`, `linux.*`, `mac.*`, `banners.*`, `yarascan.*`).

## Exemplo
```bash
# Identificar os metadados do kernel, arquitetura, build e tabela de simbolos PDB de um dump de memoria Windows
vol -f /cases/memdumps/wkst-fin-09.raw windows.info.Info
```

## Limites e trade-offs
No primeiro uso após adicionar novos pacotes `.zip` de símbolos no diretório `volatility3/symbols/`, o Volatility 3 constrói o índice de cache local de símbolos (o que pode levar alguns minutos na primeira execução, mas fica instantâneo nas execuções seguintes).

## Como verificar
Execute `vol -h` e rode `windows.info.Info` (ou `banners.Banners` para Linux) sobre uma amostra de teste para validar a resolução automática da tabela de símbolos.

## Conexões
- [[volatility3-geracao-simbolos-linux-macos-dwarf2json-vmlinux-system-map]] — Veja também: Volatility 3: Geração de Tabelas de Símbolos **ISF** para Kernels Linux e macOS com `dwarf2json`.
- [[volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline]] — Referência cruzada direta com volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
