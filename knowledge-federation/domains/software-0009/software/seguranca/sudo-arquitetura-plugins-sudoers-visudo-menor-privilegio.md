---
id: software.seguranca.tranche07.000671
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/sudo-project/sudo/main/README.md", "https://www.sudo.ws/docs/man/sudoers.man/", "https://www.sudo.ws/docs/man/sudo_logsrvd.man/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sudo (`sudo`): Arquitetura Modular de Plugins (`sudo.conf`, `sudoers.so`), Validação Sintática com **`visudo -c`** e Menor Privilégio

## Em uma frase
**Sudo** (`sudo-project/sudo`, licença ISC, mantido por Todd C. Miller) é o utilitário padrão em sistemas Linux e Unix para delegação controlada de privilégios e auditoria completa de comandos administrativos.

## Por que importa
Em vez de compartilhar a senha da conta `root` entre múltiplos administradores (o que destrói a rastreabilidade individual de quem executou qual ação e impede revogação granular), o `sudo` autentica o usuário invocador, avalia a política de segurança e registra cada comando e sessão de terminal.

## Como funciona
Desde a série 1.8/1.9, o `sudo` possui uma arquitetura modular regida por **`/etc/sudo.conf`**, carregando plugins independentes para decisão de política (`sudoers_policy`), auditoria (`sudoers_audit`), gravação de entrada/saída de terminal (`sudoers_io`) e interceptação de chamadas `execve` (`sudo_noexec.so`), enquanto os fragmentos de regras em **`/etc/sudoers.d/`** devem sempre ser validados e editados exclusivamente com **`visudo`** (`visudo -cf /etc/sudoers.d/regra`).

## Exemplo
```bash
# Validar a sintaxe e as permissoes (0440 root:root) de todos os arquivos sudoers em modo estrito (-c -s)
sudo visudo -c -s
sudo -V | head -n 15
```

## Limites e trade-offs
Conforme documentado no manual oficial `sudoers(5)`, a partir do Sudo 1.9.3 o argumento `error_recovery=true` tenta ignorar apenas a linha com erro sintático, mas configurar `Plugin sudoers_audit sudoers.so sudoers_mode=0440 error_recovery=false` em `/etc/sudo.conf` e validar com `visudo -c -s` no CI/Ansible é obrigatório para impedir comportamentos inesperados.

## Como verificar
Nunca edite `/etc/sudoers` diretamente com `vim` ou `nano` sem o wrapper `visudo`, que faz trava de concorrência e aborta a gravação se houver qualquer erro gramatical.

## Conexões
- [[sudo-gramatica-regras-sudoers-aliases-ordem-precedencia-ultima-regra]] — Veja também: Sudoers: Gramática de Especificação de Comandos, Aliases (`User_Alias`, `Runas_Alias`, `Host_Alias`, `Cmnd_Alias`) e a Regra **"Last Match Wins"**.
- [[sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp]] — Referência cruzada direta com sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
