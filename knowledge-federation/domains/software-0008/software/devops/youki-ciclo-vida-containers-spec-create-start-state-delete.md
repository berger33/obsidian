---
id: software.devops.tranche08.000734
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

# Youki: geração de especificação (youki spec) e operações de ciclo de vida OCI (create, state, start, list, delete)

## Em uma frase
O `youki` implementa o fluxo completo de gerenciamento de OCI bundles desde a geração do `config.json` com `youki spec` até as transições de estado com `youki create -b`, `youki state`, `youki start`, `youki list` e `youki delete`.

## Por que importa
Para passar nos testes de conformidade da Open Container Initiative e nos testes end-to-end do `containerd`, um runtime em Rust precisa seguir exatamente a mesma máquina de estados (`creating` -> `created` -> `running` -> `stopped`) e a mesma semântica de linha de comando esperada pelos shims de containers. A seção `Tutorial` do README oficial do `youki` demonstra passo a passo esse ciclo de vida.

## Como funciona
Primeiro, cria-se o diretório do bundle (`mkdir -p tutorial/rootfs`), exporta-se um sistema de arquivos raiz (por exemplo, `busybox`) para `rootfs/` e executa-se `../youki spec` dentro do diretório `tutorial`, gerando o arquivo `config.json` padrão. Após editar o campo `process.args` no `config.json` (por exemplo, para `["sleep", "30"]`), o operador executa a partir da raiz: (1) `sudo ./youki create -b tutorial tutorial_container` para criar os namespaces e cgroups do container; (2) `sudo ./youki state tutorial_container` para verificar que o estado do container é `"created"`; (3) `sudo ./youki start tutorial_container` para iniciar o processo; (4) `sudo ./youki list` para ver o container em estado `"running"`; e (5) `sudo ./youki delete tutorial_container` após o término para remover o container.

## Exemplo
```bash
# Preparar um OCI bundle em tutorial/, gerar config.json com youki spec e executar o ciclo create -> state -> start -> list -> delete
mkdir -p tutorial/rootfs
cd tutorial && ../youki spec && cd ..
sudo ./youki create -b tutorial tutorial_container
sudo ./youki state tutorial_container
sudo ./youki start tutorial_container
sudo ./youki list
sudo ./youki delete -f tutorial_container
```

## Limites e trade-offs
Se o processo dentro do container ainda estiver em execução (`sleep 30` em estado `running`), chamar `sudo ./youki delete tutorial_container` sem a flag `-f` (`--force`) falhará conforme determina a especificação OCI, pois um container ativo deve primeiro parar ou receber `delete -f` para ser encerrado e limpo.

## Como verificar
Execute `sudo ./youki state tutorial_container` logo após `create` e confirme que o JSON retornado na saída padrão indica `"status": "created"` e o caminho correto do bundle.

## Conexões
- [[youki-compilacao-just-dependencias-linux-rust]] — Veja também: Youki: requisitos de compilação (Rust edition 2024, Linux >= 5.3), dependências de sistema e automação com just.
- [[youki-containers-rootless-integracao-docker-podman]] — Veja também: Youki: execução de containers em modo rootless e integração com Docker e Podman.
- [[youki-runtime-oci-rust-seguranca-memoria]] — Referência cruzada direta com youki-runtime-oci-rust-seguranca-memoria.
- [[runc-ciclo-vida-create-start-list-delete-run]] — Referência cruzada direta com runc-ciclo-vida-create-start-list-delete-run.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://youki-dev.github.io/youki/user/basic_setup.html) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
