---
id: software.devops.tranche08.000732
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

# Youki: análise de desempenho e benchmark de ciclo de vida com hyperfine frente ao runc e crun

## Em uma frase
Nos benchmarks oficiais reproduzíveis com `hyperfine` documentados no README do `youki`, um ciclo completo da criação à exclusão do container leva em média `111.5 ms` no `youki` (v0.3.3), contra `224.6 ms` no `runc` (v1.1.7) e `47.3 ms` no `crun` (v1.15).

## Por que importa
Em cargas de trabalho que criam e destroem containers em altíssima frequência (como jobs curtos de CI/CD, funções FaaS ou suítes de testes efêmeros) ou em dispositivos de borda com restrições severas de memória, o tempo e a memória gastos pelo próprio runtime OCI em `create`, `start` e `delete` impactam diretamente a latência percebida. O README oficial do `youki` fornece tanto os números quanto a metodologia exata para que qualquer engenheiro reproduza o benchmark em seu próprio hardware.

## Como funciona
Para medir o custo puro do runtime OCI sem interferência de cache de disco ou de daemons externos, o benchmark oficial utiliza a ferramenta **`hyperfine`** com `--warmup 10 --min-runs 100` e um comando `--prepare` que sincroniza discos e limpa o page cache do kernel (`sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`) antes de medir a sequência `sudo ./youki create -b tutorial a && sudo ./youki start a && sudo ./youki delete -f a`. Em um ambiente Ubuntu 22.04.4 LTS (kernel 6.5.0-35-generic, 16 cores), o `runc` levou o dobro do tempo médio do `youki` (`200%`), enquanto o `youki` entregou execução rápida e consistente em Rust memory-safe.

## Exemplo
```bash
# Reproduzir o benchmark oficial do ciclo create -> start -> delete do youki usando hyperfine
hyperfine --prepare 'sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches' \
  --warmup 10 --min-runs 100 \
  'sudo ./youki create -b tutorial a && sudo ./youki start a && sudo ./youki delete -f a'
```

## Limites e trade-offs
O comando `--prepare 'sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches'` descarta todo o cache de páginas, dentries e inodes do kernel Linux no host a cada execução; portanto, esse comando de benchmark jamais deve ser executado em um servidor compartilhado de produção, pois causará degradação imediata de I/O de disco para todos os demais processos na máquina.

## Como verificar
Em uma máquina de laboratório Linux com `hyperfine` instalado e um OCI bundle em `tutorial/`, execute o benchmark comparando `./youki`, `runc` e `crun` compilados em modo release (`just youki-release`).

## Conexões
- [[youki-runtime-oci-rust-seguranca-memoria]] — Veja também: Youki: implementação da especificação OCI Runtime em Rust na CNCF.
- [[youki-compilacao-just-dependencias-linux-rust]] — Veja também: Youki: requisitos de compilação (Rust edition 2024, Linux >= 5.3), dependências de sistema e automação com just.
- [[youki-ciclo-vida-containers-spec-create-start-state-delete]] — Referência cruzada direta com youki-ciclo-vida-containers-spec-create-start-state-delete.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://youki-dev.github.io/youki/user/basic_setup.html) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
