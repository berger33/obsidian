---
id: software.seguranca.tranche12.001121
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/mitre/caldera/master/README.md", "https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **MITRE Caldera (`mitre/caldera`)**: Plataforma Automatizada de Emulação de Adversários, C2 Assíncrono e Ecossistema de Plugins

## Em uma frase
Enquanto o **Atomic Red Team** executa testes atômicos individuais em um host local, como emular de forma autônoma uma **campanha completa de um grupo APT ou ransomware** — onde o agente descobre dinamicamente usuários, diretórios e hosts vizinhos, encadeia técnicas com base nos fatos descobertos e se move lateralmente pela rede de laboratório?

## Por que importa
Desenvolvido pela **MITRE** (e mantido sob governança aberta Apache/MITRE), o **Caldera** é uma plataforma de segurança cibernética para **emulação automatizada de adversários, assistência a Red Teams e resposta automatizada a incidentes**, construída sobre o framework **MITRE ATT&CK**!

## Como funciona
Sua arquitetura é dividida em dois componentes: **(1) O Core System** (servidor Command-and-Control `C2` assíncrono em Python 3.10+ com API RESTful completa, motor de planejamento e interface Web VueJS **Magma** no Caldera v5); e **(2) O Ecossistema de Plugins** (`sandcat`, `stockpile`, `atomic`, `emu`, `manx`, `compass`, `debrief`, `response`, `gameboard`, `human`, `caldera-ot`)!

## Exemplo
```bash
# Clonar recursivamente o MITRE Caldera (incluindo todos os plugins submódulos) e iniciar o servidor v5 com compilacao da UI Magma
git clone https://github.com/apache/caldera.git --recursive
cd caldera
python3 -m venv .calderavenv && source .calderavenv/bin/activate
pip3 install -r requirements.txt
python3 server.py --insecure --build
```

## Limites e trade-offs
Ao rodar em Docker, o Caldera oferece duas variantes de imagem: **`full`** (que já embute todos os repositórios dos plugins `emu` e `atomic` para operação *offline / air-gapped*) e **`slim`** (que baixa dados sob demanda).

## Como verificar
Em implantações permanentes de laboratório, nunca use `python3 server.py --insecure` exposto na rede corporativa: habilite o plugin **`ssl`** (HTTPS), persista `conf/local.yml` (onde ficam as chaves de criptografia e senhas geradas) e restrinja o acesso à porta `8888`.

## Conexões
- [[caldera-agentes-sandcat-manx-ragdoll-c2-contacts-paw]] — Veja também: Agentes do Caldera (**`Sandcat`**, **`Manx`** e **`Ragdoll`**): Identificadores **`paw`**, Canais de Contato C2 (**HTTP, TCP, DNS, Gist**) e Grupos Red/Blue.
- [[caldera-abilities-adversary-profiles-planners-facts-parsers]] — Referência cruzada direta com caldera-abilities-adversary-profiles-planners-facts-parsers.
- [[atomicredteam-integracao-mitre-caldera-vectr-cobertura-attack-navigator]] — Referência cruzada direta com atomicredteam-integracao-mitre-caldera-vectr-cobertura-attack-navigator.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
