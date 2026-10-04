---
id: software.seguranca.tranche08.000788
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/bee-san/RustScan/master/README.md", "https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml", "https://github.com/bee-san/RustScan/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# RustScan em Containers **Docker (`rustscan/rustscan`)**: Configuração de `--network host`, `ulimit` do Container e Montagem de Volumes para o Nmap

## Em uma frase
Como a imagem oficial de container do RustScan (**`rustscan/rustscan:latest`**) já vem empacotada com o binário `rustscan` compilado **mais uma instalação completa do `nmap` e seus scripts NSE dentro do container**, muitas equipes de segurança a utilizam para não precisar instalar dependências na máquina host.

## Por que importa
Porém, ao executar um scanner de portas de alta concorrência dentro do Docker, há três detalhes de engenharia de containers importantes: **(1)** usar **`--network host`** em Linux para evitar o gargalo da ponte NAT `docker0` e do proxy `userland-proxy` em 65.535 conexões; **(2)** passar **`--ulimit nofile=10000:10000`** para o próprio `docker run` caso o daemon Docker tenha um hard limit baixo; e **(3)** montar um volume **`-v "$(pwd):/cases"`** se você passar `-oA /cases/resultado` após o `--` para que os relatórios do Nmap não sejam perdidos quando o container `--rm` for destruído!

## Como funciona
Conforme recomendado no `README.md` oficial do RustScan, criar um alias no shell (`alias rustscan='docker run -it --rm --network host --ulimit nofile=10000:10000 -v "$PWD:/cases" rustscan/rustscan:2.1.1'`) permite invocar o container de forma transparente como se fosse um binário nativo.

## Exemplo
```bash
# Executar o RustScan + Nmap via container Docker oficial com rede host e volume montado para persistir os relatorios do Nmap
docker run --rm -it \
  --network host \
  --ulimit nofile=10000:10000 \
  -v "/cases/pentest:/cases/pentest" \
  rustscan/rustscan:2.1.1 \
  -a 10.10.10.50 -b 2000 -- -sV -sC -oA /cases/pentest/docker_scan
```

## Limites e trade-offs
Lembre-se de que se você passar `-a /cases/pentest/targets.txt` para o container Docker do RustScan, o arquivo `targets.txt` também precisa estar dentro do diretório montado com `-v` para que o processo dentro do container consiga lê-lo!

## Como verificar
Verifique no diretório local `/cases/pentest/` a geração dos arquivos `docker_scan.nmap`, `.xml` e `.gnmap` após o término do container.

## Conexões
- [[rustscan-motor-scripts-customizados-rustscan-scripts-toml-python-lua]] — Veja também: RustScan **Scripting Engine (`--scripts custom`)**: Automação Pós-Descoberta em Python, Shell, Lua ou Binários via **`.rustscan_scripts.toml`**.
- [[rustscan-comparacao-arquitetural-rustscan-vs-masscan-vs-nmap-vs-zmap]] — Veja também: Decisão Arquitetural de Scanners de Portas: Quando Usar **RustScan** vs **Masscan** vs **ZMap** vs **Nmap** em Engajamentos Reais.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile]] — Referência cruzada direta com rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
