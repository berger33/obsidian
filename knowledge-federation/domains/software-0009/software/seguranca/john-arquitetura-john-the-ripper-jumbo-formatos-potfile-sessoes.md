---
id: software.seguranca.tranche15.001451
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

# Arquitetura do **John the Ripper Jumbo (`openwall/john`)**: Autodetecção de Centenas de Hashes, CPU SIMD (`AVX2`/`AVX512`) / OpenMP / OpenCL, `john.pot` e `--restore`

## Em uma frase
Criado por Solar Designer (Openwall) e expandido pela comunidade na edição **John the Ripper Jumbo (`1.9.0-Jumbo` / `bleeding-jumbo`)**, por que o **John the Ripper (`john`)** continua sendo — ao lado do Hashcat — uma das ferramentas mais indispensáveis do mundo para **Auditoria de Senhas, Pentest Interno e Forense Digital (DFIR)**?

## Por que importa
Enquanto outras ferramentas exigem que você descubra e informe códigos numéricos para cada variante de hash e dependem exclusivamente de GPUs, o **John the Ripper Jumbo**: **(1) Autodetecta mais de 400 formatos de hashes, tickets Kerberos, chaves privadas e arquivos criptografados**; **(2) Possui mais de 100 utilitários extratores nativos (`*2john`: `ssh2john`, `zip2john`, `rar2john`, `keepass2john`, `bitlocker2john`, `office2john`, `pdf2john`, `dmg2john`)**.

## Como funciona
**(3) Roda com altíssima eficiência tanto em CPUs multi-core (otimizado com `AVX2`/`AVX-512` e `OpenMP`) quanto em GPUs (`-opencl`)**; e **(4) Executa automaticamente seus 3 modos clássicos em sequência (`Single Crack` -> `Wordlist` -> `Incremental`)** quando invocado simplesmente como `john hashes.txt`!

## Exemplo
```bash
# Listar os formatos suportados pelo John Jumbo, auditar um arquivo de hashes salvando sessao nomeada (--session) e exibir as senhas recuperadas (--show)
john --list=formats | head -n 10
john --session=auditoria_ad --format=NT ./hashes_ntds.txt
john --show --format=NT ./hashes_ntds.txt
```

## Limites e trade-offs
Como funcionam os dois arquivos de estado essenciais do John (`$JOHN/john.pot` e `$JOHN/john.rec`) documentados no `README.md`? Toda senha quebrada é salva imediatamente em **`john.pot`** (e usada automaticamente nas próximas execuções para não gastar CPU tentando quebrar de novo hashes já resolvidos!); e a cada 10 minutos (ou ao apertar **`q`** ou `Ctrl+C` uma vez), o John grava o ponto exato da sessão em **`john.rec`** (ou `<nome_sessao>.rec`), permitindo retomar exatamente de onde parou a qualquer momento com **`john --restore=auditoria_ad`**!

## Como verificar
Use **`john --test=5 --format=sha512crypt`** para fazer benchmark da velocidade de hashing (em `c/s` — candidatos por segundo) dos núcleos SIMD/OpenMP da sua CPU ou GPU OpenCL.

## Conexões
- [[john-unshadow-auditoria-senhas-unix-linux-etc-passwd-shadow-crypt]] — Veja também: Auditoria de Senhas Linux/UNIX com **`unshadow`** e `john`: Entendendo Hashes **`yescrypt` (`$y$`)**, **`sha512crypt` (`$6$`)**, **`bcrypt` (`$2b$`)** e Uso dos Campos GECOS.
- [[john-extratores-2john-ssh2john-zip2john-keepass2john-office-pdf]] — Referência cruzada direta com john-extratores-2john-ssh2john-zip2john-keepass2john-office-pdf.
- [[john-modo-single-crack-gecos-username-sementes-mangling-rapido]] — Referência cruzada direta com john-modo-single-crack-gecos-username-sementes-mangling-rapido.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
