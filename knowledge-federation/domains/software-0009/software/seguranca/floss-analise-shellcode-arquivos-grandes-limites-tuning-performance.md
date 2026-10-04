---
id: software.seguranca.tranche13.001238
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
fontes: ["https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md", "https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Analisando **Shellcodes (`-f sc32`/`sc64`)** e Binários Gigantes (**`-L` / `--large-file`**, `--max-strings`, `--max-address-space`) no FLOSS

## Em uma frase
Às vezes, autores de malware inflam deliberadamente o tamanho de um executável malicioso para **50 MB ou 100 MB** (*Binary Bloating* / *Overlay Padding*) justamente para fazer sandboxes, antivírus e ferramentas de análise estática desistirem por limite de tamanho ou *timeout*! Em outros casos, você extraiu um **Shellcode bruto de 4 KB** da memória de um processo comprometido ou de um documento malicioso e quer extrair as *Stack Strings* de dentro dele.

## Por que importa
Como o **FLOSS** lida com esses dois extremos?

## Como funciona
Para **Shellcodes brutos** (que não têm cabeçalho PE/ELF), passe a flag de formato **`-f sc32`** (para shellcode x86 de 32 bits) ou **`-f sc64`** (para shellcode x86_64 de 64 bits): o FLOSS desmonta e emula o shellcode diretamente para extrair todas as *Stack Strings* e *Tight Strings* (que são o método padrão de armazenar nomes de DLLs e URLs em shellcodes!). E para **Binários Gigantes (*Binary Bloating*)**, passe a flag **`-L` (`--large-file`)** (que eleva o limite padrão de tamanho de arquivo analisável) ou combine **`--no decoded`** / **`--max-strings`** / **`--max-insn-count`** para controlar o tempo máximo de emulação!

## Exemplo
```bash
# Extrair stack/tight strings de um shellcode x64 bruto (-f sc64) e analisar um binario inflado (>16 MB) usando a flag -L (--large-file)
floss -f sc64 -v ./dumps/cobalt_beacon_stager.bin
floss -L --interesting ./amostras/bloated_dropper_80mb.exe
```

## Limites e trade-offs
Se um binário foi artificialmente inflado (*bloated*) apenas com megabytes de zeros ou lixo anexados ao final do arquivo PE (*PE Overlay*) para passar de 100 MB, lembre-se de que as strings estáticas e de Go/Rust (`floss -L --only static language`) levam apenas poucos segundos para rodar mesmo em arquivos enormes!

## Como verificar
Use **`--max-insn-count 20000`** se quiser limitar o número máximo de instruções que o emulador `vivisect` executa por chamada de função ao extrair *Decoded Strings*.

## Conexões
- [[floss-integracao-ida-pro-ghidra-binary-ninja-relatorio-html]] — Veja também: Anotando Automaticamente Desmontadores (**IDA Pro, Ghidra, Binary Ninja e x64dbg**) com os Scripts Gerados pelo FLOSS.
- [[floss-criacao-regras-yara-ioc-hunting-a-partir-strings-desofuscadas]] — Veja também: Armadilha Clássica em **Regras YARA**: Por que Usar *Decoded Strings* do FLOSS em Regras YARA de Disco Falha (e Como Usar para Caça em Memória!).
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.
- [[floss-desofuscacao-stack-strings-tight-strings-construcao-pilha-x86]] — Referência cruzada direta com floss-desofuscacao-stack-strings-tight-strings-construcao-pilha-x86.
- [[capa-analise-multi-formato-pe-elf-dotnet-shellcode-assinaturas-flirt]] — Referência cruzada direta com capa-analise-multi-formato-pe-elf-dotnet-shellcode-assinaturas-flirt.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
