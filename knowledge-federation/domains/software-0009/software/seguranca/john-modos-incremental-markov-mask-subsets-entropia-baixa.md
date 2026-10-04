---
id: software.seguranca.tranche15.001456
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

# Modos Avançados Sem Dicionário no John the Ripper: **`Incremental` (Frequência de Trigramas `.chr`)**, **`Markov`**, **`Mask` (`?u?l?l?l?d?d?d?s`)** e **`Subsets`**

## Em uma frase
Quando as senhas alvo não estão em nenhum dicionário e não derivam do nome do usuário, como o **John the Ripper** explora a probabilidade estatística da língua humana e padrões corporativos através dos modos **`Incremental`**, **`Markov`**, **`Mask`** e **`Subsets`** documentados em `doc/MODES`?

## Por que importa
Veja a diferença entre cada um: **(1) `Incremental` (`--incremental=ASCII` / `Alnum` / `Digits`)** — diferente de um força-bruta "burro" (`aaaa`, `aaab`, `aaac`), o modo Incremental usa tabelas pré-calculadas de **Frequência de Trigramas (`.chr` files)** separadas por comprimento e posição de caractere, testando primeiro as combinações de 3 letras mais prováveis de existir em senhas reais!; **(2) `Markov` (`--markov`)** — cadeias de Markov baseadas no peso probabilístico de cada caractere seguir o anterior; **(3) `Mask` (`--mask='?u?l?l?l?l2026!'`)** — máscaras posicionais e **Hybrid Wordlist + Mask (`?w2026?s`)**!; e **(4) `Subsets` (`--subsets`)**!

## Como funciona
O modo **`--subsets`** é brilhante contra usuários que tentam burlar políticas de comprimento mínimo repetindo apenas 2 ou 3 caracteres no teclado (ex.: `121212121212` ou `asasasasasas`): ele testa senhas muito longas formadas por poucos caracteres únicos antes de testar senhas curtas com muitos caracteres distintos!

## Exemplo
```bash
# Executar ataque hibrido Wordlist + Mask (?w representa a palavra do dicionario seguida de 4 digitos e 1 simbolo) e testar o modo Subsets
john --wordlist=./palavras_base.txt --mask='?w?d?d?d?d?s' --min-length=8 ./hashes.txt
john --subsets --max-length=14 ./hashes.txt
```

## Limites e trade-offs
Olhe o placeholder **`?w`** (ou `?W` com case invertido na primeira letra!) dentro do `--mask='?w?d?d?d?d?s'` do John the Ripper acima: ele permite combinar qualquer modo de entrada (`--wordlist` ou até `--single`!) com geração de máscara em GPU (`GPU-side mask acceleration`) — se o dicionário tiver 10.000 palavras e a máscara adicionar `?d?d?d?d`, a GPU multiplica cada palavra pelos 10.000 sufixos diretamente nos registradores da placa de vídeo!

## Como verificar
Você também pode gerar seu próprio arquivo de trigramas `.chr` customizado a partir do histórico de senhas da sua língua/região usando **`john --make-charset=portugues.chr`**!

## Conexões
- [[john-extratores-2john-ssh2john-zip2john-keepass2john-office-pdf]] — Veja também: A Suíte de Extratores **`*2john`** do John Jumbo: Auditando Chaves Privadas SSH (`ssh2john`), Cofres (`keepass2john`), Arquivos `.zip`/`.7z`/`.rar` e Documentos Office/PDF.
- [[john-auditoria-kerberos-active-directory-krb5tgs-asrep-ntds-dit]] — Veja também: Auditoria de Hashes de **Active Directory e Kerberos** no John Jumbo: **`NT` (`ntds.dit`)**, **Kerberoasting (`krb5tgs`)**, **AS-REP Roasting (`krb5asrep`)** e **`DCC2` (`mscash2`)**.
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Referência cruzada direta com john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes.
- [[john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom]] — Referência cruzada direta com john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
