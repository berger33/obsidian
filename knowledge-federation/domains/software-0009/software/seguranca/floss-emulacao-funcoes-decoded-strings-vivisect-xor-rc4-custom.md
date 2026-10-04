---
id: software.seguranca.tranche13.001233
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

# Extração de **Decoded Strings** no FLOSS: Identificando Heurísticas de Funções de Decodificação e Emulando a CPU com **`vivisect`**

## Em uma frase
Muitas famílias de malware corporativo (como loaders, rats, bankers e ransomwares) armazenam todas as suas strings sensíveis cifradas em uma tabela global no binário (usando `XOR` com chave multibyte, `RC4`, `ADD/ROL` ou cifras customizadas) e chamam uma função dedicada — por exemplo, `decrypt_string(cipher_ptr, len, key)` — centenas de vezes ao longo do programa sempre que precisam usar uma string.

## Por que importa
Engenheiros reversos costumavam gastar horas escrevendo scripts IDAPython ou Ghidra sob medida para cada amostra a fim de encontrar todas as referências cruzadas (`xrefs`) para `decrypt_string`, ler os argumentos passados e decodificar cada string.

## Como funciona
O motor de **Decoded Strings** do **FLOSS** automatiza 100% desse trabalho sem que você precise escrever uma única linha de código! Primeiro, ele usa heurísticas estruturais para **identificar quais funções do binário têm maior probabilidade de serem rotinas de decodificação de strings** (por exemplo: funções chamadas dezenas de vezes a partir de lugares diferentes do programa e que contêm loops de manipulação de bytes/memória). Em seguida, para cada chamada (`xref`) encontrada para essas funções candidatas, o FLOSS tira um snapshot do contexto, **emula as instruções reais da CPU usando o emulador `vivisect` (`viv_utils`)** e compara a memória RAM antes e depois da função retornar — capturando todas as strings recém-descriptografadas na memória!

## Exemplo
```bash
# Emular exclusivamente funcoes de decodificacao ou especificar manualmente o endereco de uma funcao de descriptografia descoberta no Ghidra
floss --only decoded -v ./amostras/encrypted_rat.exe
floss --functions 0x401500 0x401820 ./amostras/encrypted_rat.exe
```

## Limites e trade-offs
Olhe que recurso extraordinário na segunda linha do exemplo acima (**`floss --functions 0x401500`**): se o malware chama a rotina de decodificação apenas 2 vezes (abaixo do limiar heurístico automático) mas você identificou visualmente no Ghidra/capa que `0x401500` é a função de descriptografia, basta passar **`--functions 0x401500`** e o FLOSS emulará automaticamente todas as chamadas para `0x401500` e imprimirá as strings decodificadas!

## Como verificar
Combine `-vv` com `--functions` se quiser ver o endereço exato de cada chamada e o ponteiro de memória onde cada string foi decodificada.

## Conexões
- [[floss-desofuscacao-stack-strings-tight-strings-construcao-pilha-x86]] — Veja também: Como o FLOSS Reconstrói **Stack Strings** e **Tight Strings**: Desfazendo a Ofuscação de Strings Montadas Caractere por Caractere na Pilha da CPU.
- [[floss-extracao-strings-go-rust-utf8-estruturas-slice-sem-null-byte]] — Veja também: Análise de Binários Modernos em **Go (`Golang`)** e **Rust** com o FLOSS: Extraindo Strings de Estruturas `StringHeader` / Slices sem Terminador `\x00`.
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.
- [[capa-filtros-restricao-escopo-tags-functions-processes-otimizacao]] — Referência cruzada direta com capa-filtros-restricao-escopo-tags-functions-processes-otimizacao.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
