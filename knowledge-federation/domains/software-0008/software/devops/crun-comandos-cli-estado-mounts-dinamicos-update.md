---
id: software.devops.tranche07.000692
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

# Containers crun: comandos de ciclo de vida OCI, diretórios de estado, mounts dinâmicos e update de recursos

## Em uma frase
A CLI do `crun` implementa todos os comandos padrão OCI (`create`, `start`, `run`, `exec`, `kill`, `delete`, `list`, `state`, `ps`, `pause`, `resume`, `spec`, `update`) e adiciona subcomandos experimentais `mounts add` e `mounts remove` para alterar volumes com o container em execução.

## Por que importa
Em operações avançadas de containers, além do ciclo de vida básico, administradores precisam ajustar limites de CPU/memória/PIDs a quente sem reiniciar o processo (`crun update`), enviar sinais ou remover múltiplos containers usando expressões regulares (`--regex`) ou anexar/desanexar pontos de montagem dinamicamente em um container já em execução (`crun mounts add/remove`). A página de manual oficial `crun.1.md` especifica todas essas operações e o gerenciamento de estado.

## Como funciona
Por padrão, quando executado como usuário `root`, o `crun` salva o estado dos containers sob o diretório `/run/crun`; quando executado como usuário não privilegiado (rootless), ele respeita a variável de ambiente `XDG_RUNTIME_DIR` e utiliza `$XDG_RUNTIME_DIR/crun` (ambos podendo ser sobrescritos pela opção global `--root=DIR`). O comando `crun update` altera restrições de recursos em tempo real (como `--memory`, `--memory-swap`, `--cpu-quota`, `--cpu-period`, `--cpuset-cpus`, `--pids-limit` ou lendo de um arquivo via `-r / --resources=FILE`). Já os comandos experimentais `crun mounts add <container-id> <mounts.json>` e `crun mounts remove <container-id> <mounts.json>` permitem adicionar ou remover montagens em um container ativo passando um arquivo JSON com a seção `mounts` da configuração OCI.

## Exemplo
```bash
# Listar containers gerenciados pelo crun, atualizar o limite de memória e PIDs a quente e verificar o estado
crun list
crun update --memory 268435456 --pids-limit 512 meu-container-id
crun state meu-container-id
```

## Limites e trade-offs
Conforme documentado em `crun.1.md`, os subcomandos `mounts add` e `mounts remove` são recursos experimentais sujeitos a alterações sem aviso prévio; além disso, nos comandos `create` e `run`, a flag `--no-pivot` (que usa `chroot(2)` em vez de `pivot_root(2)`) é explicitamente marcada como **não segura** na documentação oficial e deve ser evitada em produção.

## Como verificar
Inicie um container com `crun`, execute `crun ps <container-id> --format=json` e `crun state <container-id>` e confirme a leitura precisa dos processos e do estado a partir de `/run/crun` (ou `$XDG_RUNTIME_DIR/crun`).

## Conexões
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Veja também: Containers crun: runtime OCI escrito inteiramente em C para alta performance e baixo footprint de memória.
- [[crun-logging-global-options-journald-syslog-json]] — Veja também: Containers crun: opções globais de diagnóstico, backends de log (file, journald, syslog) e formatos text/json.
- [[runc-ciclo-vida-create-start-list-delete-run]] — Referência cruzada direta com runc-ciclo-vida-create-start-list-delete-run.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
