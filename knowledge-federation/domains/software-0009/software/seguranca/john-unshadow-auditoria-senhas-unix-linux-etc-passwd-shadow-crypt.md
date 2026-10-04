---
id: software.seguranca.tranche15.001452
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

# Auditoria de Senhas Linux/UNIX com **`unshadow`** e `john`: Entendendo Hashes **`yescrypt` (`$y$`)**, **`sha512crypt` (`$6$`)**, **`bcrypt` (`$2b$`)** e Uso dos Campos GECOS

## Em uma frase
Quando um administrador de segurança precisa auditar a força das senhas locais de um servidor Linux, por que é recomendável **combinar `/etc/passwd` e `/etc/shadow` usando o utilitário nativo `unshadow`** em vez de passar apenas o arquivo `/etc/shadow` puro para o **John the Ripper**?

## Por que importa
Porque o arquivo `/etc/shadow` contém apenas o login e o hash (`usuario:$y$j9T$...`), enquanto o arquivo **`/etc/passwd`** contém o **Campo GECOS (Nome Completo, Cargo, Departamento, Telefone)** e o caminho do diretório Home!

## Como funciona
Quando você executa **`unshadow /etc/passwd /etc/shadow > shadow_combinado.txt`**, o utilitário funde os dois arquivos no formato clássico UNIX: com isso, logo no primeiro segundo de execução (no modo **`Single Crack`**), o John the Ripper extrai o nome real, sobrenome, iniciais e login de cada usuário do campo GECOS e testa milhares de variações (`Carlos2026!`, `c.silva123`) **especificamente contra o hash daquele usuário**, descobrindo senhas baseadas em nomes pessoais instantaneamente!

## Exemplo
```bash
# Combinar /etc/passwd e /etc/shadow com unshadow (protegendo com chmod 0600) e auditar senhas fracas Linux (yescrypt/sha512crypt) com o John
umask 077
unshadow /etc/passwd /etc/shadow > ./auditoria_shadow.txt
john --single ./auditoria_shadow.txt
john --show ./auditoria_shadow.txt
```

## Limites e trade-offs
Identifique pelo prefixo modular (`$id$`) qual algoritmo `crypt(3)` protege as senhas no `/etc/shadow` do seu Linux: **`$y$`** é o moderno **`yescrypt`** (padrão no Debian 11+, Ubuntu 22.04+, Fedora 35+ e RHEL 9/10 — *memory-hard*, altíssima resistência a GPUs e ASICs!); **`$6$`** é o **`sha512crypt`** (5.000 rodadas de SHA-512 por padrão); e **`$2b$` / `$2y$`** é o **`bcrypt`** (Blowfish)!

## Como verificar
Se durante a auditoria você encontrar qualquer servidor antigo ainda usando `$1$` (`md5crypt`) ou `rounds=` abaixo do padrão, migre imediatamente no `/etc/pam.d/common-password` (`pam_unix.so yescrypt`)!

## Conexões
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Veja também: Arquitetura do **John the Ripper Jumbo (`openwall/john`)**: Autodetecção de Centenas de Hashes, CPU SIMD (`AVX2`/`AVX512`) / OpenMP / OpenCL, `john.pot` e `--restore`.
- [[john-modo-single-crack-gecos-username-sementes-mangling-rapido]] — Veja também: O Poder do Modo **`"Single crack"` (`--single`)** e **`--single-seed`** no John the Ripper: Quebrando Senhas Corporativas Contextualizadas em Segundos.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
