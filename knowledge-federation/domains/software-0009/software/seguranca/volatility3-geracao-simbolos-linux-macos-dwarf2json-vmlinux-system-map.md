---
id: software.seguranca.tranche06.000532
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

# Volatility 3: Geração de Tabelas de Símbolos **ISF** para Kernels Linux e macOS com `dwarf2json`

## Em uma frase
Enquanto para o Windows o Volatility 3 baixa e converte automaticamente os arquivos de símbolos `.pdb` públicos dos servidores da Microsoft, em **Linux** cada distribuição e atualização de kernel altera o layout das estruturas C internas (`task_struct`, `mm_struct`, `module`), exigindo gerar o arquivo JSON **ISF** exato daquele kernel com o utilitário oficial **`dwarf2json`** (`volatilityfoundation/dwarf2json`, Go).

## Por que importa
Sem o arquivo ISF correspondente à string exata do banner do kernel Linux capturado na memória (identificada pelo plugin `banners.Banners`), o Volatility 3 não consegue localizar os offsets das listas de processos e sockets na RAM.

## Como funciona
O `dwarf2json linux` processa o binário do kernel compilado com símbolos de depuração DWARF (`--elf /usr/lib/debug/boot/vmlinux-<versao>`, proveniente dos pacotes `linux-image-*-dbgsym` no Ubuntu/Debian ou `kernel-debuginfo` no RHEL/Fedora) e opcionalmente a tabela de endereços `--system-map /boot/System.map-<versao>` (que tem precedência máxima para resolver offsets exatos com KASLR), gerando o JSON ISF que deve ser salvo em `volatility3/symbols/linux/`.

## Exemplo
```bash
# Identificar o banner exato do kernel no dump de RAM e gerar o arquivo ISF correspondente com dwarf2json
vol -f /cases/memdumps/prod-k8s-node01.lime banners.Banners

./dwarf2json linux \
  --elf /usr/lib/debug/boot/vmlinux-5.15.0-122-generic \
  --system-map /boot/System.map-5.15.0-122-generic \
  | xz -c > volatility3/symbols/linux/ubuntu-5.15.0-122-generic.json.xz
```

## Limites e trade-offs
Processar arquivos `vmlinux` grandes com informações completas de depuração DWARF no `dwarf2json` consome bastante memória (a documentação oficial recomenda no mínimo **8 GB de RAM** na máquina de geração do símbolo); comprima o `.json` gerado com `.xz` ou `.gz` para economizar disco.

## Como verificar
Execute `vol -f /cases/memdumps/prod-k8s-node01.lime linux.pslist.PsList` após colocar o arquivo `.json.xz` em `volatility3/symbols/linux/` e confirme a listagem dos processos do kernel.

## Conexões
- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Veja também: Volatility 3: Arquitetura de Análise Forense de Memória RAM, *Intermediate Symbol Format* (`ISF`) e *Translation Layers*.
- [[volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline]] — Veja também: Volatility 3: Análise de Processos Windows (`pslist`, `pstree`, `psscan`, `cmdline`, `envars` e Detecção de *DKOM*).
- [[volatility3-forense-linux-rootkits-check-syscall-modules-bash-sockstat]] — Referência cruzada direta com volatility3-forense-linux-rootkits-check-syscall-modules-bash-sockstat.
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Referência cruzada direta com capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
