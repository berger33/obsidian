---
id: software.seguranca.tranche15.001457
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

# Auditoria de Hashes de **Active Directory e Kerberos** no John Jumbo: **`NT` (`ntds.dit`)**, **Kerberoasting (`krb5tgs`)**, **AS-REP Roasting (`krb5asrep`)** e **`DCC2` (`mscash2`)**

## Em uma frase
Como usar o **John the Ripper Jumbo** durante uma auditoria autorizada de Active Directory para testar a resistência das senhas de contas de serviço (**Kerberoasting `krb5tgs`**, **AS-REP Roasting `krb5asrep`**), hashes **NTLM (`--format=NT`)** extraídos do `ntds.dit` e credenciais cacheadas de domínio (**Domain Cached Credentials v2 — `--format=mscash2`**)?

## Por que importa
O John Jumbo suporta nativamente todos os formatos de autenticação Windows/Kerberos gerados pelo **Impacket (`GetUserSPNs.py`, `GetNPUsers.py`, `secretsdump.py`)** e pelo **NetExec (`nxc`)**: **(1) `--format=krb5tgs`** (ou `krb5tgs-opencl` para tickets TGS `RC4-HMAC` etype 23, `AES128-CTS-HMAC-SHA1-96` etype 17 e `AES256` etype 18); **(2) `--format=krb5asrep`** (respostas AS-REP de contas com *Do not require Kerberos preauthentication*).

## Como funciona
**(3) `--format=NT`** (hashes NTLM diretos); e **(4) `--format=mscash2`** (`PBKDF2-HMAC-SHA1` com 10.240 iterações padrão do Windows)!

## Exemplo
```bash
# Auditar tickets Kerberoasting (krb5tgs) e hashes NTLM do Active Directory com o John Jumbo e gerar estatisticas de contas quebradas
john --format=krb5tgs --wordlist=./dicionario_corporativo.txt --rules=KoreLogic ./tickets_kerberoast.txt
john --show --format=krb5tgs ./tickets_kerberoast.txt
```

## Limites e trade-offs
Por que auditar o arquivo `ntds.dit` (formato `domain\uid:rid:lmhash:nthash:::`) com o modo **`john --single --format=NT`** descobre dezenas de contas de serviço e de usuários logo nos primeiros 30 segundos? Porque o parser do John lê o nome da conta (`svc_backup_sql`, `joao.ferreira`) da primeira coluna do dump do `secretsdump.py` e testa instantaneamente variações do próprio nome da conta como senha!

## Como verificar
Para mitigar 100% o risco de quebra de senhas de contas de serviço via **Kerberoasting** no Active Directory, migre contas de serviço para **Group Managed Service Accounts (`gMSA`)** (que possuem senhas aleatórias de 240 bytes rotacionadas automaticamente a cada 30 dias) e desative o `RC4-HMAC (etype 23)` exigindo `AES-256 (etype 18)`.

## Conexões
- [[john-modos-incremental-markov-mask-subsets-entropia-baixa]] — Veja também: Modos Avançados Sem Dicionário no John the Ripper: **`Incremental` (Frequência de Trigramas `.chr`)**, **`Markov`**, **`Mask` (`?u?l?l?l?d?d?d?s`)** e **`Subsets`**.
- [[john-modos-externos-compilador-c-embutido-external-filter-custom]] — Veja também: O Compilador C Embutido do John the Ripper (**`External Mode` — `doc/EXTERNAL`**): Escrevendo Geradores e Filtros de Candidatos (`--external`) em Subconjunto de C.
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Referência cruzada direta com john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
