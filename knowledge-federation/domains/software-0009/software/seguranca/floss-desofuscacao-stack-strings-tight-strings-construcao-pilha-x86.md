---
id: software.seguranca.tranche13.001232
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

# Como o FLOSS Reconstrói **Stack Strings** e **Tight Strings**: Desfazendo a Ofuscação de Strings Montadas Caractere por Caractere na Pilha da CPU

## Em uma frase
Uma das técnicas favoritas de autores de malware e implantes em C/C++ para esconder nomes de DLLs (`kernel32.dll`, `ntdll.dll`), funções (`VirtualAlloc`) ou endereços de C2 do comando `strings` e de regras YARA simples é usar **Stack Strings** (por exemplo: `char url[8]; url[0]='h'; url[1]='t'; url[2]='t'; url[3]='p'; ...`). No código de máquina x86/x64 compilado, cada caractere vira uma instrução individual `mov byte ptr [ebp-10h], 68h` espalhada pelo código, de modo que a string nunca existe contígua no disco!

## Por que importa
Uma variante ainda mais capciosa é a **Tight String (*Tight Loop Stack String*)**, onde o compilador ou o atacante coloca um array de bytes ofuscados na pilha e executa um pequeno loop local (*tight loop*) dentro da própria função para fazer `XOR`/`ADD`/`SUB` em cada byte na pilha antes de usar a string!

## Como funciona
Como o **FLOSS** derrota ambas as técnicas? Para **Stack Strings**, o FLOSS analisa o grafo de fluxo de controle de cada função, monitora o estado do ponteiro de pilha (`ESP`/`RSP`/`EBP`/`RBP`) ao longo de cada bloco básico e reconstrói o conteúdo exato do buffer de pilha no momento em que ele é passado como argumento para uma chamada de função (`call`)! E para **Tight Strings**, ele detecta funções com *tight loops* que modificam variáveis locais na pilha e **emula a execução do loop até que a string completa apareça limpa na pilha**!

## Exemplo
```bash
# Extrair exclusivamente Stack Strings e Tight Strings de um binario suspeito (pulando strings estaticas comuns para execucao rapida)
floss --only stack tight ./amostras/stealth_loader.exe
```

## Limites e trade-offs
As flags **`--only`** e **`--no`** do FLOSS (que aceitam `static`, `language`, `stack`, `tight`, `decoded`) permitem escolher exatamente quais motores de extração rodar: passar `--only stack tight decoded` foca 100% nas strings que o autor do malware tentou esconder deliberadamente!

## Como verificar
No modo verboso (**`floss -v`**), o FLOSS imprime ao lado de cada Stack String e Tight String o **endereço virtual exato da função (`0x4012A0`)** onde ela foi construída!

## Conexões
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Veja também: Arquitetura do **Mandiant FLOSS (`mandiant/flare-floss`)**: Superando o `strings` Tradicional com Extração de **Stack Strings, Tight Strings, Decoded Strings e Go/Rust**.
- [[floss-emulacao-funcoes-decoded-strings-vivisect-xor-rc4-custom]] — Veja também: Extração de **Decoded Strings** no FLOSS: Identificando Heurísticas de Funções de Decodificação e Emulando a CPU com **`vivisect`**.
- [[capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction]] — Referência cruzada direta com capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
