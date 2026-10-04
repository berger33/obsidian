---
id: software.seguranca.tranche15.001432
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
fontes: ["https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md", "https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Políticas Modulares em **`/etc/fapolicyd/rules.d/`**, Compilador **`fagenrules`** e Diferença entre os Perfis **`known-libs`** e **`restrictive`** no fapolicyd

## Em uma frase
Como o **`fapolicyd`** organiza suas regras de decisão, como o script **`fagenrules`** monta a política final e qual é a diferença arquitetural entre as duas políticas oficiais documentadas no `README.md`: **`known-libs` (padrão)** e **`restrictive`**?

## Por que importa
As regras do `fapolicyd` são divididas em arquivos numerados dentro de **`/etc/fapolicyd/rules.d/*.rules`** (ex.: `20-dracut.rules`, `21-updaters.rules`, `30-patterns.rules`, `40-bad-elf.rules`, `41-shared-obj.rules`, `42-trusted-elf.rules`, `70-trusted-lang.rules`, `72-shell.rules`, `90-deny-execute.rules`, `95-allow-open.rules`). Quando o serviço inicia (ou quando você roda **`fagenrules --load`**), os fragmentos são concatenados em `/etc/fapolicyd/compiled.rules` e avaliados **de cima para baixo, onde a primeira regra que casar vence (*First Match Wins*)**!

## Como funciona
Na política **`known-libs` (padrão)**: **(1)** Impede bypass via invocação direta do linker dinâmico (`ld.so`); **(2)** Tudo o que pede execução (`perm=execute`) deve estar no banco de confiança (`trust=1`); e **(3)** Qualquer biblioteca compartilhada (`.so`) ou módulo/script Python/Perl/Shell aberto por um interpretador deve ser confiável (`trust=1`)! Já na política **`restrictive`**, além disso, **apenas binários ELF, Python e Shell scripts confiáveis são habilitados por padrão**, bloqueando outras linguagens a menos que explicitamente adicionadas!

## Exemplo
```bash
# Verificar se houve mudanca nos fragmentos de /etc/fapolicyd/rules.d/, compilar e recarregar as regras a quente no daemon com fagenrules
fagenrules --check
fagenrules --load
fapolicyd-cli --list
```

## Limites e trade-offs
Por que a regra que bloqueia a invocação direta do **`ld.so`** (`/lib64/ld-linux-x86-64.so.2 /tmp/malware.elf`) é o pilar número 1 das políticas do `fapolicyd`? Porque quando alguém executa `/lib64/ld-linux-x86-64.so.2 /tmp/malware.elf`, do ponto de vista do Kernel a chamada `execve()` está executando o `/lib64/ld-linux-x86-64.so.2` (que é um arquivo confiável do sistema!) e apenas abrindo (`perm=open`) o `/tmp/malware.elf` como argumento! As regras `30-patterns.rules` (`pattern=ld_so`) e `41-shared-obj.rules` do `fapolicyd` detectam e bloqueiam essa técnica clássica de evasão!

## Como verificar
E atenção ao aviso de depreciação oficial do `fapolicyd`: a macro antiga `dir=untrusted` está depreciada; novas regras devem sempre validar **`trust=1` / `trust=0`** explicitamente sobre o objeto.

## Conexões
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Veja também: Arquitetura do **fapolicyd (`linux-application-whitelisting/fapolicyd` — *File Access Policy Daemon*)**: **Application Whitelisting** no Linux via Kernel **`fanotify`** e Banco **`LMDB`**.
- [[fapolicyd-sintaxe-regras-decision-perm-subject-object-customizacao]] — Veja também: A Receita de Escrita de Regras no fapolicyd: **`decision perm subject : object`**, Tipos MIME (`ftype`), `trust=1` e `deny_audit`.
- [[fapolicyd-modo-permissivo-debug-deny-testes-seguros-producao]] — Referência cruzada direta com fapolicyd-modo-permissivo-debug-deny-testes-seguros-producao.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
