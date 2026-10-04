---
id: software.devops.tranche08.000739
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/youki-dev/youki/main/README.md", "https://youki-dev.github.io/youki/user/basic_setup.html", "https://github.com/youki-dev/youki"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Youki: validação nos testes end-to-end do containerd e uso como runtime em clusters Kubernetes

## Em uma frase
O `youki` é validado contra a suíte de testes end-to-end (e2e) do `containerd` e pode ser configurado como handler de runtime OCI no `containerd` ou `CRI-O` para executar Pods em clusters Kubernetes de produção.

## Por que importa
Um runtime OCI que funciona em exemplos simples de linha de comando ainda pode falhar quando submetido às exigências reais de um nó Kubernetes — como criação simultânea de sandboxes CRI, anexação de volumes CNI/CSI, probes `exec` concorrentes, coleta de métricas de cgroup v2 e limpeza sob pressão de recursos. Conforme destaca a seção `Status of youki` do README oficial, o `youki` superou os testes e2e do `containerd` e já é adotado em ambientes de produção.

## Como funciona
Para utilizar o `youki` em um nó Kubernetes com `containerd`, o administrador instala o binário `youki` em `/usr/local/bin/youki` (ou `/usr/bin/youki`) e registra um handler em `/etc/containerd/config.toml` sob `[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.youki]` utilizando `runtime_type = "io.containerd.runc.v2"` e apontando `BinaryName = "/usr/local/bin/youki"` em `.options`. Como o `youki` implementa a mesma interface CLI OCI que o `runc`, o `containerd-shim-runc-v2` padrão consegue invocá-lo diretamente quando um Pod especifica `runtimeClassName: youki`.

## Exemplo
```toml
# Trecho de /etc/containerd/config.toml registrando o youki como runtime OCI para o containerd-shim-runc-v2
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.youki]
  runtime_type = "io.containerd.runc.v2"
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.youki.options]
    BinaryName = "/usr/local/bin/youki"
    SystemdCgroup = true
```

## Limites e trade-offs
Quando `SystemdCgroup = true` é configurado no `containerd` para nós Kubernetes que usam `cgroup v2` unificado e systemd, o binário do `youki` precisa ter sido compilado com suporte a `libsystemd` (incluído nas instruções oficiais de dependências do README) para negociar a criação de scopes com o systemd do host.

## Como verificar
Após registrar o handler `youki` no `containerd` e criar o objeto `RuntimeClass` correspondente no Kubernetes, inicie um Pod de teste com `runtimeClassName: youki` e verifique que ele atinge o estado `Running`.

## Conexões
- [[youki-desenvolvimento-multiplataforma-vagrant-codespaces-testes-oci]] — Veja também: Youki: ambientes de desenvolvimento com Vagrant (rootless e rootful), GitHub Codespaces e testes de integração OCI.
- [[youki-inspecao-capacidades-kernel-bpf-checkpoint-restore-info]] — Veja também: Youki: diagnóstico de capacidades do host (CAP_BPF, CAP_PERFMON, CAP_CHECKPOINT_RESTORE) e cgroups via youki info.
- [[youki-runtime-oci-rust-seguranca-memoria]] — Referência cruzada direta com youki-runtime-oci-rust-seguranca-memoria.
- [[youki-arquitetura-interna-libcontainer-crates-workspaces]] — Referência cruzada direta com youki-arquitetura-interna-libcontainer-crates-workspaces.
- [[crun-gerenciamento-cgroups-v2-systemd-subgroup-delegation]] — Referência cruzada direta com crun-gerenciamento-cgroups-v2-systemd-subgroup-delegation.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://youki-dev.github.io/youki/user/basic_setup.html) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
