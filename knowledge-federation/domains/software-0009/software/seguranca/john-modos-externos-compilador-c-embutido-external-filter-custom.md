---
id: software.seguranca.tranche15.001458
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

# O Compilador C Embutido do John the Ripper (**`External Mode` — `doc/EXTERNAL`**): Escrevendo Geradores e Filtros de Candidatos (`--external`) em Subconjunto de C

## Em uma frase
Você sabia que o **John the Ripper** possui um **Compilador de Linguagem C Embutido (Bytecode VM)** que compila e executa funções escritas em uma seção **`[List.External:<NOME>]`** do `john.conf` no momento em que o programa inicia?

## Por que importa
Conforme documentado em `doc/MODES` e `doc/EXTERNAL`, os **Modos Externos (`--external=<MODO>`)** operam de duas maneiras: **(1) Como um Gerador de Senhas (`init()`, `generate()`, `restore()`)** — quando a lógica da senha segue um algoritmo proprietário ou matemático específico (por exemplo, senhas padrão de roteadores que incluem um dígito verificador de Luhn ou CPF/CNPJ válido!) que nenhuma máscara simples consegue expressar; e **(2) Como um Filtro de Política (`filter()`)** combinado com `--wordlist` ou `--incremental`!

## Como funciona
Quando usado como **Filtro (`filter()`)**, cada candidato gerado pelo `--wordlist` ou `--incremental` passa primeiro pela sua função `filter()` em C: se o candidato **não** atender à política de complexidade do alvo (ex.: o Active Directory do alvo exige obrigatoriamente pelo menos 1 maiúscula, 1 minúscula, 1 número e 1 símbolo com mínimo de 10 caracteres!), a função define `word = 0;` e **o John nem perde tempo calculando o hash caro (`bcrypt`/`mscash2`) daquele candidato inválido**!

## Exemplo
```bash
# Listar todos os modos externos e filtros pre-instalados no john.conf e usar o filtro externo Policy junto com wordlist
john --list=externals
john --wordlist=./dicionario.txt --rules=Jumbo --external=Filter_Alpha ./hashes.txt
```

## Limites e trade-offs
Veja na saída de **`john --list=externals`** dezenas de modos e filtros prontos de fábrica no `john.conf`: `Filter_Alpha`, `Filter_Digits`, `Filter_Alnum`, `AutoAbort`, `AutoStatus`, `Parallel` (para dividir trabalho entre múltiplos nós sem sobreposição!), `Keyboard` (caminhadas pelo layout físico do teclado `qwerty`!) e `DateTime`!

## Como verificar
Combinar um modo de geração com um **`--external=Filter_*`** em hashes lentos (`Argon2`, `bcrypt`, `PBKDF2`, `LUKS`) economiza até 80% do tempo de auditoria ao pular todas as senhas que o sistema alvo jamais teria permitido cadastrar!

## Conexões
- [[john-auditoria-kerberos-active-directory-krb5tgs-asrep-ntds-dit]] — Veja também: Auditoria de Hashes de **Active Directory e Kerberos** no John Jumbo: **`NT` (`ntds.dit`)**, **Kerberoasting (`krb5tgs`)**, **AS-REP Roasting (`krb5asrep`)** e **`DCC2` (`mscash2`)**.
- [[john-execucao-distribuida-fork-node-mpi-opencl-gpu-aceleracao]] — Veja também: Escalando o John the Ripper em Múltiplos Núcleos, GPUs e Clusters: **`--fork=N`**, **`--node=MIN-MAX/TOTAL`**, OpenMP e Formatos **`-opencl`**.
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Referência cruzada direta com john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes.
- [[john-modos-incremental-markov-mask-subsets-entropia-baixa]] — Referência cruzada direta com john-modos-incremental-markov-mask-subsets-entropia-baixa.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
