---
id: software.seguranca.tranche12.001144
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/aide/aide/master/README", "https://aide.github.io/doc/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ciclo Operacional do AIDE: **`--init`**, **`--check`**, **`--update`**, **`--compare`** e Interpretação dos **Códigos de Retorno (`1` a `7`)** em Scripts

## Em uma frase
Como operar o ciclo de vida do banco de dados do AIDE no dia a dia de administração de servidores Linux e interpretar programaticamente seus códigos de saída (`exit codes`) em pipelines de automação e monitoramento?

## Por que importa
O fluxo operacional consiste em três fases: **(1) Inicialização (`aide --init`)** — varre o sistema de arquivos recém-instalado e grava o snapshot inicial em `database_out` (`/var/lib/aide/aide.db.new.gz`), que você então promove para `database_in` (`mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz`); **(2) Verificação diária (`aide --check`)** — compara o estado atual do disco contra o `aide.db.gz`; e **(3) Atualização pós-janela de manutenção (`aide --update`)** — após aplicar patches legítimos do `apt`/`dnf`, executa a verificação e gera simultaneamente um novo `aide.db.new.gz` atualizado!

## Como funciona
O `aide --check` e `aide --update` utilizam **códigos de retorno em máscara de bits (*bitmask*)** para informar exatamente o que mudou: **`0`** (nenhuma alteração detectada), **`1`** (arquivos adicionados), **`2`** (arquivos removidos), **`3`** (`1+2`: adicionados e removidos), **`4`** (arquivos modificados), **`5`** (`1+4`: adicionados e modificados), **`6`** (`2+4`: removidos e modificados) e **`7`** (`1+2+4`: adicionados, removidos e modificados)! Códigos `>= 14` indicam erros de execução/configuração.

## Exemplo
```bash
# Inicializar o banco de dados do AIDE, promove-lo para producao e executar uma verificacao capturando o bitmask de retorno
sudo aide --config=/etc/aide/aide.conf --init
sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
sudo aide --config=/etc/aide/aide.conf --check ; echo "Exit code AIDE: $?"
```

## Limites e trade-offs
Nunca automatize a substituição cega de `aide.db.gz` por `aide.db.new.gz` em um cronjob diário sem revisão humana ou correlação com uma janela aprovada de gerência de mudanças (Ansible/apt/dnf): se o banco for sobrescrito automaticamente toda noite, qualquer backdoor plantada por um invasor passará a fazer parte do baseline "limpo" no dia seguinte!

## Como verificar
Use `aide --compare` quando quiser comparar dois arquivos de banco de dados históricos (`database_in` vs `database_new`) offline em uma estação de auditoria.

## Conexões
- [[aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros]] — Veja também: Regras de Seleção e Expressões Regulares PCRE2 no **`aide.conf`**: Seleções Regulares (`/caminho`), Restritas (`=/caminho`), Negativas (`!/caminho`) e Macros.
- [[aide-monitoramento-logs-crescentes-growing-size-rotacao-logrotate]] — Veja também: Monitoramento de Integridade de **Arquivos de Log (`S` / `ANF` / `ARF`)** no AIDE: Como Detectar Truncamento de Logs sem Falsos Positivos no `logrotate`.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.
- [[aide-regras-atributos-hashes-acl-xattrs-selinux-e2fsattrs-aide-conf]] — Referência cruzada direta com aide-regras-atributos-hashes-acl-xattrs-selinux-e2fsattrs-aide-conf.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
