---
id: software.seguranca.tranche10.000952
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/sashs/Ropper/master/README.md", "https://raw.githubusercontent.com/sashs/Ropper/master/Ropper.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ropper: Inspeção de Cabeçalhos Binários (**`-i`, `-e`, `--imagebase`, `-s`, `-S`, `--imports`, `--symbols`**) e Filtro **Microsoft Control Flow Guard (`--cfg-only`)**

## Em uma frase
Além de buscar gadgets, o Ropper funciona como um inspetor multi-formato para executáveis **Linux (`ELF`)**, **Windows (`PE` / `.exe` / `.dll`)** e **macOS (`Mach-O`)**.

## Por que importa
Com as flags de informação do Ropper, você audita rapidamente: **`-i` / `--info`** (arquitetura, endianness, proteções **NX** e **ASLR/PIE**), **`-e`** (endereço de *EntryPoint*), **`--imagebase`** (endereço base padrão onde o binário é mapeado), **`-s` / `--sections`** e **`-S` / `--segments`** (seções e segmentos com tamanhos e permissões), **`--imports`** (funções importadas da `libc` ou de DLLs do Windows na IAT/PLT) e **`--symbols`**!

## Como funciona
Para binários **PE do Windows (`-c` / `--dllcharacteristics`)** compilados com a mitigação moderna **Microsoft Control Flow Guard (CFG)**, o Ropper possui a flag exclusiva **`--cfg-only`**, que filtra apenas os gadgets cujos endereços de entrada passam na verificação de bitmap do CFG!

## Exemplo
```bash
# Inspecionar cabecalhos de seguranca (-i), ImageBase (--imagebase), secoes (-s) e funcoes importadas (--imports) de um binario
ropper --file /cases/pwn/vuln_service --info --imagebase --sections --imports
```

## Limites e trade-offs
O Ropper também permite ativar ou desativar os bits de mitigação **NX e ASLR** diretamente no cabeçalho de binários de laboratório/CTF usando **`--set nx`**, **`--unset nx`**, **`--set aslr`** ou **`--unset aslr`** para testar como um exploit se comporta com e sem cada mitigação!

## Como verificar
Se você descobriu em runtime (via information leak) que uma biblioteca compartilhada com PIE/ASLR foi carregada no endereço `0x7ffff7a00000`, passe **`-I 0x7ffff7a00000`** para que o Ropper já some esse `ImageBase` em todos os gadgets impressos!

## Conexões
- [[ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes]] — Veja também: **Ropper (`sashs/Ropper`)**: Arquitetura Multi-Formato (**ELF, PE, Mach-O, Raw**) e Busca de Gadgets **ROP, JOP e SYS** sobre **Capstone & `filebytes`**.
- [[ropper-busca-avancada-gadgets-ppr-stack-pivot-badbytes-qualidade]] — Veja também: Ropper: Busca Avançada de Gadgets (**`--search`**, `--quality`, **`--stack-pivot`**, `-p` `pop-pop-ret`, `-j` `jmp reg`) e Filtro de **`--badbytes` (`-b`)**.
- [[pwndbg-auditoria-mitigacoes-binarias-checksec-vmmap-aslr-pie-nx-canary]] — Referência cruzada direta com pwndbg-auditoria-mitigacoes-binarias-checksec-vmmap-aslr-pie-nx-canary.

## Fontes
- [Ropper Official GitHub — Multi-Architecture ROP/JOP/SYS Gadget Finder, Semantic Search (PyVEX/Z3) & Python API (`RopperService`)](https://raw.githubusercontent.com/sashs/Ropper/master/README.md) — documentação oficial completa do Ropper cobrindo formatos ELF/PE/Mach-O/Raw, 10 arquiteturas, busca semântica Z3, geradores de ROP chains, badbytes e API `RopperService`; consultado em 2026-10-03.
- [Ropper Official CLI Entrypoint & Source (`Ropper.py`)](https://raw.githubusercontent.com/sashs/Ropper/master/Ropper.py) — código-fonte oficial de inicialização do Ropper e integração com `filebytes`; consultado em 2026-10-03.
