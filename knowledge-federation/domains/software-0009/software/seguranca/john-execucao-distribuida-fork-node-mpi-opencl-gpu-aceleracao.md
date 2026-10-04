---
id: software.seguranca.tranche15.001459
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md", "https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Escalando o John the Ripper em Múltiplos Núcleos, GPUs e Clusters: **`--fork=N`**, **`--node=MIN-MAX/TOTAL`**, OpenMP e Formatos **`-opencl`**

## Em uma frase
Como distribuir uma auditoria de senhas pesada com o **John the Ripper** entre todos os núcleos de um servidor multi-socket, entre múltiplas placas de vídeo (**GPUs via OpenCL**) ou até mesmo entre **10 máquinas diferentes na rede sem precisar de um servidor central**?

## Por que importa
O John Jumbo oferece 4 mecanismos nativos de paralelismo: **(1) `OpenMP`** (ativo por padrão na maioria dos formatos lentos de CPU, controlável via variável `OMP_NUM_THREADS`); **(2) `--fork=N`** — lança `N` processos filhos independentes na mesma máquina dividindo automaticamente as palavras/candidatos entre eles (muitas vezes mais rápido que OpenMP em formatos rápidos ou sistemas NUMA!); **(3) `--format=<formato>-opencl --devices=1,2`** — despacha o cálculo para GPUs NVIDIA/AMD/Intel via OpenCL!; e **(4) `--node=MIN-MAX/TOTAL`**!

## Como funciona
A flag **`--node=MIN-MAX/TOTAL`** permite distribuir qualquer trabalho entre várias máquinas independentes sem comunicação de rede entre elas: basta rodar na Máquina 1 `--node=1/4`, na Máquina 2 `--node=2/4`, na Máquina 3 `--node=3/4` e na Máquina 4 `--node=4/4` — cada máquina processa exatamente `1/4` do espaço de chaves sem nunca repetir um único candidato!

## Exemplo
```bash
# Listar os formatos acelerados por GPU (-opencl) e executar uma auditoria dividida entre 4 processos (--fork=4) ou em um cluster de 3 nos (--node)
john --list=formats --format=opencl | head -n 10
john --fork=4 --wordlist=./dicionario.txt --rules=best64 ./hashes.txt
```

## Limites e trade-offs
Quando você usa **`--fork=4`**, o John cria arquivos de recuperação numerados para cada processo worker (`john.rec`, `john.2.rec`, `john.3.rec`, `john.4.rec`) e todos compartilham de forma segura o mesmo arquivo `john.pot`!

## Como verificar
Se você estiver auditando hashes rápidos (como `NT`, `Raw-SHA256`, `krb5tgs`) em GPU com `-opencl`, alimente um volume grande de candidatos por palavra (usando `--rules=Jumbo` ou `--mask`) para manter os milhares de *Shader Cores* da GPU 100% saturados.

## Conexões
- [[john-modos-externos-compilador-c-embutido-external-filter-custom]] — Veja também: O Compilador C Embutido do John the Ripper (**`External Mode` — `doc/EXTERNAL`**): Escrevendo Geradores e Filtros de Candidatos (`--external`) em Subconjunto de C.
- [[john-expressao-dinamica-dynamic-formats-auditoria-estatisticas-relatorio]] — Veja também: Formatos Dinâmicos Customizados (**`--format=dynamic=...`**) e Análise Estatística de Senhas Quebradas no John the Ripper.
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Referência cruzada direta com john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes.
- [[john-modos-incremental-markov-mask-subsets-entropia-baixa]] — Referência cruzada direta com john-modos-incremental-markov-mask-subsets-entropia-baixa.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
