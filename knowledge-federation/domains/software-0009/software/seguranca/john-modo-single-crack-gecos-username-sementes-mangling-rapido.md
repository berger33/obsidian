---
id: software.seguranca.tranche15.001453
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

# O Poder do Modo **`"Single crack"` (`--single`)** e **`--single-seed`** no John the Ripper: Quebrando Senhas Corporativas Contextualizadas em Segundos

## Em uma frase
Por que a documentação oficial do John (`doc/MODES`) afirma categoricamente sobre o **`"Single crack" mode`**: *"This is the mode you should start cracking with"* (Este é o modo com o qual você deve começar)?

## Por que importa
Porque no modo `--wordlist` comum, cada palavra da wordlist precisa ser hasheada para **todos os salts diferentes** do arquivo de entrada. Já no modo **`--single`**, o John pega as palavras derivadas dos metadados da própria conta (login `carlos.mendes`, nome completo no GECOS `Carlos Eduardo Mendes`, nome da pasta home) e aplica um conjunto gigantesco de regras de mutação (*Mangling Rules*) **apenas contra o salt daquela conta específica** — tornando o teste milhares de vezes mais rápido por conta! E assim que o `--single` descobre a senha de um usuário, ele automaticamente testa aquela senha descoberta contra todos os outros hashes carregados (`--single-retest-guess`)!

## Como funciona
Mais poderoso ainda em auditorias corporativas é a opção **`--single-seed=Palavra1,Palavra2`** (ou `--single-wordlist=arquivo.txt`) documentada em `doc/MODES`!

## Exemplo
```bash
# Executar o modo Single Crack injetando sementes contextuais da empresa (--single-seed: nome da empresa, cidade, sigla e ano) combinadas com os logins
john --single --single-seed=EmpresaX,Guarulhos,2026,Mudar ./auditoria_shadow.txt
```

## Limites e trade-offs
Entenda o que acontece quando você passa **`--single-seed=EmpresaX,Guarulhos,2026,Mudar`** no comando acima: o John the Ripper combina automaticamente essas palavras-semente da cultura da empresa com o login/nome de cada funcionário e aplica todas as regras de mangling (testando `EmpresaX@2026`, `carlos.EmpresaX`, `Mudar@123`, `Guarulhos2026!` para cada conta)!

## Como verificar
Para evitar que funcionários criem senhas contendo o próprio nome de login ou o nome da empresa, ative no `pwquality.conf` do PAM as diretivas `usercheck = 1`, `gecoscheck = 1` e adicione o nome/siglas da empresa no dicionário de palavras proibidas (`dictpath`).

## Conexões
- [[john-unshadow-auditoria-senhas-unix-linux-etc-passwd-shadow-crypt]] — Veja também: Auditoria de Senhas Linux/UNIX com **`unshadow`** e `john`: Entendendo Hashes **`yescrypt` (`$y$`)**, **`sha512crypt` (`$6$`)**, **`bcrypt` (`$2b$`)** e Uso dos Campos GECOS.
- [[john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom]] — Veja também: Modo **`Wordlist` (`--wordlist`)** e Motor de **Regras de Mutação (`--rules` / `doc/RULES`)** no John the Ripper: `best64`, `KoreLogic`, `Jumbo` e Sintaxe de Regras.
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Referência cruzada direta com john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
