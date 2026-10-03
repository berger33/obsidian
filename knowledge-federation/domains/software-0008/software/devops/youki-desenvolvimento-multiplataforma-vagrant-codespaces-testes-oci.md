---
id: software.devops.tranche08.000738
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

# Youki: ambientes de desenvolvimento com Vagrant (rootless e rootful), GitHub Codespaces e testes de integração OCI

## Em uma frase
Como a compilação e execução local do `youki` exigem Linux (kernel >= 5.3), o projeto disponibiliza um `Vagrantfile` com dois perfis pré-configurados (`default` para modo rootless e `rootful` para modo rootful), suporte a GitHub Codespaces e alvo `just test-oci` para testes de conformidade OCI.

## Por que importa
Muitos contribuidores de código open-source trabalham em laptops macOS ou Windows onde as chamadas de sistema de namespaces, cgroups e `seccomp` do kernel Linux não existem nativamente; além disso, toda alteração no runtime precisa ser validada contra a suíte oficial `opencontainers/runtime-tools`. As seções `Quick Start`, `Integration Tests` e `Setting up Vagrant` do README oficial do `youki` cobrem esses fluxos.

## Como funciona
Para desenvolvedores fora do Linux, o `Vagrantfile` incluído no repositório oferece duas máquinas virtuais distintas: `vagrant up default && vagrant ssh default` sobe o ambiente configurado por padrão para desenvolvimento e testes em **modo rootless**, enquanto `vagrant up rootful && vagrant ssh rootful` sobe uma VM configurada para desenvolvimento em **modo rootful**. Alternativamente, o ambiente pode ser aberto instantaneamente na nuvem via **GitHub Codespaces** (`just build` seguido de `docker run --runtime youki hello-world`). Para rodar os testes oficiais de integração da OCI (que exigem Go e `node-tap` para executar o submódulo `opencontainers/runtime-tools`), inicializam-se os submódulos com `git submodule update --init --recursive` e executa-se `just test-oci`.

## Exemplo
```bash
# Inicializar submódulos (opencontainers/runtime-tools) e executar a suíte de testes de integração OCI no youki
git submodule update --init --recursive
just test-oci
```

## Limites e trade-offs
Executar `just test-oci` sem antes inicializar os submódulos Git (`git submodule update --init --recursive`) ou sem ter o runtime Go e o utilitário `node-tap` instalados no ambiente falhará imediatamente, pois o harness de validação de conformidade da OCI (`runtime-tools`) é escrito em Go e emite relatórios TAP.

## Como verificar
Em um ambiente Linux ou dentro da VM provisionada com `vagrant up default`, execute `just youki-dev` e valide a passagem dos testes do projeto.

## Conexões
- [[youki-arquitetura-interna-libcontainer-crates-workspaces]] — Veja também: Youki: arquitetura modular em Rust e biblioteca libcontainer para gerenciamento de namespaces, cgroups e syscalls.
- [[youki-integracao-containerd-kubernetes-e2e-producao]] — Veja também: Youki: validação nos testes end-to-end do containerd e uso como runtime em clusters Kubernetes.
- [[youki-runtime-oci-rust-seguranca-memoria]] — Referência cruzada direta com youki-runtime-oci-rust-seguranca-memoria.
- [[youki-compilacao-just-dependencias-linux-rust]] — Referência cruzada direta com youki-compilacao-just-dependencias-linux-rust.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://youki-dev.github.io/youki/user/basic_setup.html) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
