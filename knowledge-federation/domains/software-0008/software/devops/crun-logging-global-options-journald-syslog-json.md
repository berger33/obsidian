---
id: software.devops.tranche07.000693
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
fontes: ["https://raw.githubusercontent.com/containers/crun/main/README.md", "https://raw.githubusercontent.com/containers/crun/main/crun.1.md", "https://github.com/containers/crun"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Containers crun: opções globais de diagnóstico, backends de log (file, journald, syslog) e formatos text/json

## Em uma frase
O `crun` oferece opções globais de observabilidade e depuração (`--debug`, `--log`, `--log-format` e `--log-level`) com suporte nativo aos backends de log `file:PATH`, `journald:IDENTIFIER` e `syslog:IDENTIFIER`.

## Por que importa
Quando a inicialização de um container falha dentro do namespace isolado antes que o processo da aplicação comece a emitir logs padrão, capturar o motivo exato do erro de sistema (como falha em uma regra seccomp, mount SELinux negado ou limite de cgroup inválido) exige direcionar as mensagens internas do runtime OCI para o agregador de logs do host de forma estruturada. O manual oficial `crun.1.md` detalha o funcionamento dos backends e níveis de log do `crun`.

## Como funciona
A opção global `--log=BACKEND:SPECIFIER` define o destino das mensagens de erro e aviso geradas pelo `crun`, suportando três backends: `file:PATH` (padrão caso nenhum prefixo de backend seja especificado), `journald:IDENTIFIER` (enviando diretamente ao systemd-journald do host) e `syslog:IDENTIFIER`. O formato das mensagens é controlado por `--log-format=FORMAT` (`text` por padrão, ou `json` para integração com motores como CRI-O, Podman e coletores de log), enquanto `--log-level=LEVEL` ajusta a verbosidade entre `error` (padrão), `warning` e `debug` (ou ativando `--debug` diretamente). Se um erro ocorrer tardiamente no processo init do container, quando o processo pai do `crun` já parou de monitorá-lo, a mensagem é impressa no `stderr` do próprio container.

## Exemplo
```bash
# Executar um comando crun com nível de log debug estruturado em JSON gravando em arquivo de diagnóstico
crun --debug --log=file:/tmp/crun-debug.json --log-format=json --log-level=debug list
cat /tmp/crun-debug.json
```

## Limites e trade-offs
Habilitar `--debug` ou `--log-level=debug` globalmente na configuração do container runtime do nó Kubernetes (`crio.conf` ou `containerd/config.toml`) gera dezenas de entradas detalhadas a cada `create`, `start` e `exec` (incluindo probes de liveness/readiness do kubelet), podendo aumentar o uso de disco do journald; recomenda-se manter `error` em produção e ativar `debug` apenas ao diagnosticar falhas de inicialização de pods.

## Como verificar
Execute um comando `crun` passando `--log=file:/tmp/test.log --log-format=json --log-level=debug` e valide que qualquer aviso ou informação de depuração é gravado em JSON válido no arquivo especificado.

## Conexões
- [[crun-comandos-cli-estado-mounts-dinamicos-update]] — Veja também: Containers crun: comandos de ciclo de vida OCI, diretórios de estado, mounts dinâmicos e update de recursos.
- [[crun-gerenciamento-cgroups-v2-systemd-subgroup-delegation]] — Veja também: Containers crun: gerenciamento de cgroups (cgroupfs, systemd) e anotações de subgrupo e delegação em cgroup v2.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
