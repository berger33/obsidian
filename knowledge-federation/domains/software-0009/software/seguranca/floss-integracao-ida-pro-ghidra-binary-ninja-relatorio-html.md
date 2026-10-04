---
id: software.seguranca.tranche13.001237
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

# Anotando Automaticamente Desmontadores (**IDA Pro, Ghidra, Binary Ninja e x64dbg**) com os Scripts Gerados pelo FLOSS

## Em uma frase
Quando um malware usa *Stack Strings* ou uma função central de descriptografia (*Decoded Strings*), abrir o binário no **Ghidra** ou no **IDA Pro** é frustrante no início: em vez de ver comentários claros como `"https://c2.attacker.example/gate.php"` ao lado de cada chamada `call decrypt_string`, você vê apenas `call sub_401500` dezenas de vezes com ponteiros para bytes incompreensíveis!

## Por que importa
Como injetar automaticamente todas as strings desofuscadas pelo **FLOSS** diretamente como comentários nos endereços exatos das instruções e funções dentro do **IDA Pro**, **Ghidra**, **Binary Ninja** ou **x64dbg**?

## Como funciona
O repositório oficial do FLOSS (`flare-floss/scripts/`) fornece o script **`render-floss-result-script.py`** (que consome o arquivo JSON gerado por `floss -j amostra.exe > floss.json`): ele converte o resultado do FLOSS em um script Python pronto para rodar dentro do **IDA Pro / Ghidra / Binary Ninja** (ou banco de comentários do `x64dbg`), adicionando comentários repetíveis (*repeatable comments*) e anotações de Decompiler exatamente em cada endereço onde uma *Stack String*, *Tight String* ou *Decoded String* foi recuperada!

## Exemplo
```bash
# Gerar o resultado JSON do FLOSS com metadados de enderecos de funcoes pronto para anotar automaticamente o Ghidra ou IDA Pro
floss -j -v ./amostras/encrypted_implant.exe > ./implant_floss.json
jq '.strings.decoded_strings[] | {address: .address, decoded_at: .decoded_at, string: .string}' ./implant_floss.json
```

## Limites e trade-offs
Veja no comando `jq` acima os dois endereços que o FLOSS registra para cada **Decoded String**: **`address`** (o endereço da função de decodificação, ex.: `0x401500`) e **`decoded_at`** (o endereço exato da instrução `call` que chamou a decodificação para aquela string específica, ex.: `0x403218`)!

## Como verificar
Quando o script anota cada endereço `decoded_at` no Ghidra ou IDA Pro com a string limpa correspondente, a leitura do código descompilado em C passa de criptografada para cristalina em poucos segundos!

## Conexões
- [[floss-busca-filtragem-query-regex-json-html-web-viewer]] — Veja também: Busca com Expressões Regulares (**`--query`**), Exportação **`-j` JSON** e Relatório Visual Interativo (**`--html`**) no FLOSS.
- [[floss-analise-shellcode-arquivos-grandes-limites-tuning-performance]] — Veja também: Analisando **Shellcodes (`-f sc32`/`sc64`)** e Binários Gigantes (**`-L` / `--large-file`**, `--max-strings`, `--max-address-space`) no FLOSS.
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.
- [[floss-emulacao-funcoes-decoded-strings-vivisect-xor-rc4-custom]] — Referência cruzada direta com floss-emulacao-funcoes-decoded-strings-vivisect-xor-rc4-custom.
- [[capa-integracao-ida-pro-ghidra-binary-ninja-capa-explorer-web]] — Referência cruzada direta com capa-integracao-ida-pro-ghidra-binary-ninja-capa-explorer-web.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
