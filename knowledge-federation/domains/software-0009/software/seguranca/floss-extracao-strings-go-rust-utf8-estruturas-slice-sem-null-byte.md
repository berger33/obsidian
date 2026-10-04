---
id: software.seguranca.tranche13.001234
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

# Análise de Binários Modernos em **Go (`Golang`)** e **Rust** com o FLOSS: Extraindo Strings de Estruturas `StringHeader` / Slices sem Terminador `\x00`

## Em uma frase
Nos últimos anos, houve uma explosão de malwares multiplataforma (ransomwares para Windows/Linux/ESXi, backdoors de nuvem e infostealers) e ferramentas de ataque escritas em **Go (`Golang`)** e **Rust**. Quando um analista roda o comando `strings` comum sobre um binário em Go ou Rust, o que acontece?

## Por que importa
O resultado é um desastre: em vez de ver strings individuais limpas, o `strings` cospe blocos gigantescos e ilegíveis de dezenas de milhares de caracteres grudados uns nos outros! Isso acontece porque, diferentemente do C (onde cada string termina com um byte nulo `\x00`), **Go e Rust armazenam strings UTF-8 em memória como fatias (*Slices*: um par `{Pointer, Length}` de 16 bytes em 64-bit) apontando para dentro de uma única tabela contígua de caracteres na seção `.rodata` / `.rdata` sem nenhum byte `\x00` separando uma string da outra**!

## Como funciona
O motor **Language-Specific Strings (`language`)** do **FLOSS** detecta automaticamente que o executável PE, ELF ou Mach-O foi compilado em **Go** ou **Rust**, localiza todas as estruturas `{Pointer, Length}` e instruções de carregamento de fatias de string no binário e **fatia com precisão cirúrgica cada string individual exatamente no seu comprimento real**!

## Exemplo
```bash
# Extrair de forma limpa todas as strings especificas de um binario compilado em Go ou Rust e auditar a taxa de cobertura (--summary)
floss --summary ./amostras/golang_ransomware.elf
```

## Limites e trade-offs
A flag **`--summary`** exibida no exemplo acima é especialmente útil para binários em **Go** e **Rust**: ela mostra um relatório estatístico informando qual porcentagem de bytes do grande *blob* de strings da linguagem já foi fatiada e recuperada pelo FLOSS, além de destacar faixas de bytes não referenciadas que merecem inspeção manual!

## Como verificar
Quando o FLOSS detecta Go ou Rust, ele executa o extrator específico da linguagem automaticamente; se você quiser forçar ou desativar esse modo, pode usar `--language go`, `--language rust` ou `--language none`.

## Conexões
- [[floss-emulacao-funcoes-decoded-strings-vivisect-xor-rc4-custom]] — Veja também: Extração de **Decoded Strings** no FLOSS: Identificando Heurísticas de Funções de Decodificação e Emulando a CPU com **`vivisect`**.
- [[floss-layout-aware-static-strings-section-structure-semantic-tags]] — Veja também: Strings Estáticas Conscientes de Layout (**Layout-Aware Static Strings**) e **Tags Semânticas (`--tag`, `--interesting`)** no FLOSS.
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.
- [[capa-analise-multi-formato-pe-elf-dotnet-shellcode-assinaturas-flirt]] — Referência cruzada direta com capa-analise-multi-formato-pe-elf-dotnet-shellcode-assinaturas-flirt.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
