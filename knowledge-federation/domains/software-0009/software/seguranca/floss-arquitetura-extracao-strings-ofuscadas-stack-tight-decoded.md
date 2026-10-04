---
id: software.seguranca.tranche13.001231
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

# Arquitetura do **Mandiant FLOSS (`mandiant/flare-floss`)**: Superando o `strings` Tradicional com Extração de **Stack Strings, Tight Strings, Decoded Strings e Go/Rust**

## Em uma frase
Por que rodar o utilitário clássico `strings` do Unix sobre um malware moderno, um binário compilado em **Go (`Golang`)** ou **Rust**, ou um implante de Red Team quase sempre falha em mostrar as URLs de Comando e Controle (C2), os nomes de APIs carregadas dinamicamente e as chaves de criptografia?

## Por que importa
Porque o comando `strings` tradicional faz apenas uma varredura ingênua procurando sequências de bytes ASCII ou UTF-16 terminadas em byte nulo (`\x00`), o que falha em dois cenários muito comuns: **(1) Ofuscação deliberada de strings pelo autor do malware** (que constrói a string caractere por caractere na pilha da CPU em tempo de execução ou a mantém cifrada em disco e só a decodifica em memória RAM quando vai usá-la!); e **(2) Layout interno de compiladores modernos como Go e Rust** (que armazenam todas as strings concatenadas em um único grande *blob* sem terminadores nulos `\x00`, referenciadas por estruturas `{ponteiro, comprimento}`)!

## Como funciona
Criado pela equipe **FLARE da Mandiant**, o **FLOSS (*FLARE Obfuscated String Solver*)** resolve ambos os problemas extraindo automaticamente **5 categorias de strings** de qualquer binário: **(1) Static Strings** (ASCII e UTF-16LE enriquecidas com layout e tags semânticas), **(2) Stack Strings**, **(3) Tight Strings**, **(4) Decoded Strings** (via emulação de CPU!) e **(5) Language-Specific Strings (Go e Rust)**!

## Exemplo
```bash
# Executar o Mandiant FLOSS sobre um binario suspeito para extrair strings estaticas, stack strings, tight strings, decoded strings e Go/Rust
floss ./amostras/suspicious_implant.exe
```

## Limites e trade-offs
Ao final da execução, o FLOSS agrupa as strings extraídas por categoria e, quando identifica que o binário foi compilado em **Go** ou **Rust**, aplica automaticamente os extratores estruturais específicos daquela linguagem!

## Como verificar
Use **`floss -n 6`** (`--minimum-length 6`) quando quiser aumentar o comprimento mínimo das strings extraídas (o padrão é `4` caracteres) para reduzir ruído visual em binários muito grandes.

## Conexões
- [[floss-desofuscacao-stack-strings-tight-strings-construcao-pilha-x86]] — Veja também: Como o FLOSS Reconstrói **Stack Strings** e **Tight Strings**: Desfazendo a Ofuscação de Strings Montadas Caractere por Caractere na Pilha da CPU.
- [[floss-emulacao-funcoes-decoded-strings-vivisect-xor-rc4-custom]] — Referência cruzada direta com floss-emulacao-funcoes-decoded-strings-vivisect-xor-rc4-custom.
- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Referência cruzada direta com capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
