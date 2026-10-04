---
id: software.seguranca.tranche15.001454
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md", "https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Modo **`Wordlist` (`--wordlist`)** e Motor de **Regras de Mutação (`--rules` / `doc/RULES`)** no John the Ripper: `best64`, `KoreLogic`, `Jumbo` e Sintaxe de Regras

## Em uma frase
Como funciona a linguagem de **Word Mangling Rules (`--rules`)** do John the Ripper — tão expressiva e compacta que sua sintaxe foi adotada posteriormente pelo próprio Hashcat — e como usar os conjuntos de regras embutidos no `john.conf` (`--rules=best64`, `--rules=KoreLogic`, `--rules=OneRuleToRuleThemAll`, `--rules=All`)?

## Por que importa
No modo `--wordlist=dicionario.txt`, se você passar **`--rules=<conjunto>`**, cada palavra do dicionário passa por um pipeline de comandos de 1 ou 2 caracteres definidos em `[List.Rules:<conjunto>]`: por exemplo, **`c`** capitaliza a primeira letra (`senha` -> `Senha`), **`$2$0$2$6$!`** anexa `2026!` ao final, **`^@`** insere `@` no início, **`sa@se3si1so0`** substitui `a->@`, `e->3`, `i->1`, `o->0` (*Leet Speak*), **`r`** inverte a palavra, **`d`** duplica (`bola` -> `bolabola`), e **`>7`** rejeita candidatos que não tenham mais de 7 caracteres!

## Como funciona
Além disso, o pré-processador de regras do John suporta intervalos compactos como **`c$[0-9]$[0-9]$[!@#$%]`**, que expande uma única linha em `10 x 10 x 5 = 500` regras de mutação automaticamente!

## Exemplo
```bash
# Visualizar na tela (--stdout) todas as mutacoes geradas por uma regra customizada do John sem executar hashing e rodar auditoria com --rules=best64
echo "seguranca" | john --stdin --rules=':c$[2]$[0]$[2]$[4-6]$[!@#]' --stdout
john --wordlist=./dicionario_corporativo.txt --rules=best64 ./hashes.txt
```

## Limites e trade-offs
Veja o truque essencial na primeira linha acima (**`john --stdin --rules='...' --stdout`**): antes de rodar uma regra nova contra hashes lentos (`bcrypt` / `Argon2` / `KeePass`), sempre teste sua regra com `--stdout` sobre uma palavra de exemplo para inspecionar exatamente quais candidatos ela gera e quantas variações por palavra são produzidas!

## Como verificar
Conforme recomendado em `doc/MODES`, prepare e deduplicite seus dicionários de entrada em letras minúsculas (`tr A-Z a-z < fonte.txt | sort -u > limpo.txt`), pois o conjunto padrão de regras de mangling do John assume palavras-base em minúsculas e se encarrega de testar todas as variações de capitalização!

## Conexões
- [[john-modo-single-crack-gecos-username-sementes-mangling-rapido]] — Veja também: O Poder do Modo **`"Single crack"` (`--single`)** e **`--single-seed`** no John the Ripper: Quebrando Senhas Corporativas Contextualizadas em Segundos.
- [[john-extratores-2john-ssh2john-zip2john-keepass2john-office-pdf]] — Veja também: A Suíte de Extratores **`*2john`** do John Jumbo: Auditando Chaves Privadas SSH (`ssh2john`), Cofres (`keepass2john`), Arquivos `.zip`/`.7z`/`.rar` e Documentos Office/PDF.
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Referência cruzada direta com john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
