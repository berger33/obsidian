---
id: software.devops.tranche08.000702
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
fontes: ["https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md", "https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md", "https://github.com/kata-containers/kata-containers"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kata Containers: suporte multi-arquitetura de virtualização e diagnóstico com kata-runtime check

## Em uma frase
O Kata Containers suporta sistemas de 64 bits em quatro arquiteturas (`x86_64`/`amd64` com Intel VT-x ou AMD SVM, `aarch64`/`arm64` com ARM Hyp, `ppc64le` com IBM Power e `s390x` com IBM Z & LinuxONE SIE) e valida o host com `kata-runtime check`.

## Por que importa
Tentar agendar Pods isolados por máquina virtual em nós Kubernetes cujas CPUs não expõem extensões de virtualização de hardware (por exemplo, instâncias de nuvem sem nested virtualization ou sem metal) causa falhas imediatas de criação de sandbox. O README oficial do Kata Containers documenta a matriz de arquiteturas suportadas e o funcionamento detalhado do utilitário de verificação `kata-runtime check`.

## Como funciona
O comando `kata-runtime check` inspeciona as flags do processador, módulos de kernel (`/dev/kvm` ou equivalente da arquitetura) e dependências de sistema para determinar se o host é capaz de criar um Kata Container. Por padrão, o comando exibe apenas uma mensagem resumida de sucesso/falha e conecta-se à rede para verificar no GitHub se há uma versão mais recente do Kata Containers disponível. O operador pode adicionar `--no-network-checks` para desativar a consulta ao GitHub e `--verbose` para listar todas as checagens realizadas; quando executado como usuário `root`, verificações adicionais de privilégio são executadas (incluindo checar se outro hipervisor incompatível está ativo) e os testes de rede são desabilitados automaticamente.

## Exemplo
```bash
# Executar validação completa de hardware como root (desativa checagens de rede automaticamente e testa hipervisores)
sudo kata-runtime check --verbose
```

## Limites e trade-offs
Executar `kata-runtime check` como um usuário comum sem privilégios de `root` em um script de automação pode tentar realizar conexões HTTP externas para a API do GitHub (que falharão em ambientes corporativos air-gapped se `--no-network-checks` for omitido) e deixará de rodar os testes profundos de conflito de hipervisor no kernel.

## Como verificar
Confirme que `sudo kata-runtime check` retorna código de saída `0` e a mensagem indicando que o sistema é capaz de executar Kata Containers na arquitetura detectada (`amd64`, `arm64`, `ppc64le` ou `s390x`).

## Conexões
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Veja também: Kata Containers: máquinas virtuais leves com isolamento de hardware e experiência de containers.
- [[kata-componentes-principais-shimv2-runtime-rs-agent-dragonball]] — Veja também: Kata Containers: componentes principais (runtime Go, runtime-rs em Rust, agent e VMM embutido dragonball).
- [[kata-hipervisores-configuracao-runtime-agent]] — Referência cruzada direta com kata-hipervisores-configuracao-runtime-agent.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
