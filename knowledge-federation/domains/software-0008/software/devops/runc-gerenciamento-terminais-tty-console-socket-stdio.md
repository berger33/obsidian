---
id: software.devops.tranche07.000690
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/opencontainers/runc/main/README.md", "https://github.com/opencontainers/runtime-spec", "https://github.com/opencontainers/runc"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenContainer runc: gerenciamento de terminais pseudo-TTY (--console-socket), descritores stdio e capabilities

## Em uma frase
O `runc` gerencia a alocação de pseudo-terminais (PTY) e fluxos de entrada/saída padrão (`stdin`, `stdout`, `stderr`) diferenciando sessões interativas (`"terminal": true` ou `--console-socket`) de execuções desacopladas em segundo plano (`"terminal": false`).

## Por que importa
Quando um orquestrador como `containerd` (via `containerd-shim`) ou `kubectl exec -ti` inicia um container com um terminal interativo, o processo que cria o PTY (`ptmx`/`pts`) roda dentro do user/mount namespace do container, mas quem precisa ler e escrever no lado mestre do PTY é o shim no host. De acordo com o README oficial do `runc` e sua documentação de terminais (`docs/terminals.md`), o mecanismo de `--console-socket` e a configuração do bloco `process` no `config.json` governam essa passagem segura de descritores.

## Como funciona
Quando `"terminal": true` está definido em `process` no `config.json` e o operador executa `runc run` diretamente no shell, o `runc` conecta o PTY recém-alocado do container ao terminal atual do usuário. Porém, quando o container é iniciado de forma desacoplada (`runc create` / `runc run -d`) por um runtime de nível superior, se `"terminal": true` for usado, o chamador deve fornecer um caminho de socket UNIX via `--console-socket /caminho/console.sock`, pelo qual o `runc` envia o descritor de arquivo do lado mestre (`ptmx`) usando `SCM_RIGHTS`. Já quando `"terminal": false`, o `runc` não aloca um PTY no container e herda os descritores `stdin`, `stdout` e `stderr` (normalmente pipes criados pelo shim para captura de logs), além de suportar `--preserve-fds` para passar descritores de arquivo adicionais para dentro do container.

## Exemplo
```bash
# Inspecionar a configuração de terminal, capabilities e rlimits no config.json de um bundle OCI
jq '{terminal: .process.terminal, args: .process.args, capabilities: .process.capabilities.effective, noNewPrivileges: .process.noNewPrivileges}' config.json
```

## Limites e trade-offs
Tentar executar `runc create` ou `runc run -d` (em background) mantendo `"terminal": true` no `config.json` sem passar `--console-socket` resultará em erro imediato do `runc` (`cannot allocate tty if runc will detach without setting console socket`), pois o container perderia o controle do terminal sem ter para quem entregar o descritor `ptmx`.

## Como verificar
Edite um `config.json` definindo `"terminal": false` e execute `sudo runc run -d --pid-file /tmp/c.pid test-bg` redirecionando `stdout`/`stderr` para um arquivo de log, confirmando que o container inicia em segundo plano sem exigir um console socket.

## Conexões
- [[runc-assinatura-releases-gpg-keyring-auditoria-seguranca]] — Veja também: OpenContainer runc: verificação de releases assinadas com runc.keyring, auditoria Cure53 e processo de segurança OCI.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.
- [[runc-oci-bundle-rootfs-config-json-runc-spec]] — Referência cruzada direta com runc-oci-bundle-rootfs-config-json-runc-spec.
- [[runc-ciclo-vida-create-start-list-delete-run]] — Referência cruzada direta com runc-ciclo-vida-create-start-list-delete-run.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
