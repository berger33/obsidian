---
id: software.seguranca.tranche13.001282
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
fontes: ["https://raw.githubusercontent.com/linux-pam/linux-pam/master/README", "https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Semântica das **Control Flags** do Linux-PAM (**`required`, `requisite`, `sufficient`, `optional`**) e Sintaxe Avançada `[success=done default=ignore]`

## Em uma frase
Qual é a diferença exata de segurança entre declarar um módulo PAM como **`required`** versus **`requisite`** versus **`sufficient`**, e por que colocar um módulo **`sufficient`** na linha errada de `/etc/pam.d/` pode criar uma vulnerabilidade grave de **Authentication Bypass**?

## Por que importa
Compreender a máquina de estados de avaliação da pilha PAM evita que um módulo opcional ou suficiente encerre prematuramente a validação de segurança.

## Como funciona
Quando a `libpam` avalia de cima para baixo as linhas de um mesmo grupo (ex.: `auth`) em `/etc/pam.d/`: **(1) `required`** — o módulo **precisa ter sucesso** para que a autenticação final seja aprovada, mas se ele falhar, **o PAM continua executando os módulos seguintes da pilha antes de retornar o erro final** (por quê? Para não revelar a um atacante remoto exatamente em qual etapa a autenticação falhou!); **(2) `requisite`** — também exige sucesso, mas se falhar, **aborta a pilha imediatamente naquele ponto** sem executar nenhum módulo subsequente (ideal para bloquear uma tentativa logo no topo antes mesmo de pedir senha ou consultar a rede!); **(3) `sufficient`** — se tiver sucesso **e nenhum módulo `required` anterior tiver falhado**, aprova imediatamente e pula o resto da pilha!; e **(4) `optional`** — só decide o resultado se for o único módulo da pilha!

## Exemplo
```text
# Comparacao classica na pilha auth: requisite aborta imediatamente se falhar; required continua a pilha mas garante falha no final
auth    requisite    pam_faillock.so preauth
auth    required     pam_unix.so nullok
auth     [default=die] pam_faillock.so authfail
auth    sufficient   pam_faillock.so authsucc
```

## Limites e trade-offs
Entenda por que a ordem de um módulo **`sufficient`** é crítica: se você colocar `auth sufficient pam_permit.so` ou um módulo de chave de hardware `sufficient` **acima** de um verificador de bloqueio de conta (`pam_faillock` ou `pam_nologin`), o sucesso do `sufficient` encerrará a pilha prematuramente com aprovação! Por isso, verificações de pré-condição no topo da pilha devem usar **`requisite`** ou **`required`**!

## Como verificar
A sintaxe entre colchetes **`[value1=action1 value2=action2 ...]`** (ex.: `[success=1 default=ignore]` ou `[default=die]`) é a forma interna completa na qual o PAM traduz as palavras-chave simples: `die` encerra imediatamente com falha, `done` encerra com o resultado atual, `ok` marca sucesso e `N` (um inteiro positivo) pula exatamente as próximas `N` linhas da pilha!

## Conexões
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Veja também: Arquitetura do **Linux-PAM (`linux-pam/linux-pam`)**: Os 4 Grupos de Gerenciamento (**`auth`, `account`, `password`, `session`**) e Arquivos `/etc/pam.d/`.
- [[pam-protecao-forca-bruta-pam-faillock-faillock-conf-bloqueio-contas]] — Veja também: Bloqueio contra Força Bruta no Linux com **`pam_faillock.so`** e **`/etc/security/faillock.conf`**: `deny`, `fail_interval`, `unlock_time` e `even_deny_root`.
- [[pam-auditoria-integridade-pam-d-prevencao-backdoors-pam-permit]] — Referência cruzada direta com pam-auditoria-integridade-pam-d-prevencao-backdoors-pam-permit.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
